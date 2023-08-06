from __future__ import annotations

from typing import TYPE_CHECKING

import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
import ai.h2o.featurestore.api.v1.FeatureSetProtoApi_pb2 as FeatureSetApi

from ..utils import Utils
from . import query
from .feature_ref import FeatureRef

if TYPE_CHECKING:  # Only imports the below statements during type checking
    from .feature_set import FeatureSet

CATEGORICAL = FeatureSetApi.FeatureType.Name(FeatureSetApi.FeatureType.CATEGORICAL)
NUMERICAL = FeatureSetApi.FeatureType.Name(FeatureSetApi.FeatureType.NUMERICAL)
TEMPORAL = FeatureSetApi.FeatureType.Name(FeatureSetApi.FeatureType.TEMPORAL)
TEXT = FeatureSetApi.FeatureType.Name(FeatureSetApi.FeatureType.TEXT)
COMPOSITE = FeatureSetApi.FeatureType.Name(FeatureSetApi.FeatureType.COMPOSITE)
AUTOMATIC_DISCOVERY = FeatureSetApi.FeatureType.Name(
    FeatureSetApi.FeatureType.AUTOMATIC_DISCOVERY
)


class Feature:
    def __init__(
        self, stub, feature_set: FeatureSet, internal_feature, absolute_feature_name
    ):
        self._stub = stub
        self._fs = feature_set
        self._internal_feature = internal_feature
        self._absolute_feature_name = absolute_feature_name

    @property
    def name(self):
        return self._internal_feature.name

    @property
    def version(self):
        return self._internal_feature.version

    @property
    def special(self):
        return self._internal_feature.special

    @special.setter
    def special(self, value):
        update_request = pb.FeatureStringFieldUpdateRequest()
        update_request.new_value = value
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureSpecial(update_request)
        self._refresh()

    @property
    def version_change(self):
        return self._internal_feature.version_change

    @property
    def status(self):
        return self._internal_feature.status

    @status.setter
    def status(self, value):
        update_request = pb.FeatureStringFieldUpdateRequest()
        update_request.new_value = value
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureStatus(update_request)
        self._refresh()

    @property
    def data_type(self):
        return self._internal_feature.data_type

    @property
    def profile(self):
        return FeatureProfile(self._stub, self._fs, self)

    @property
    def description(self):
        return self._internal_feature.description

    @description.setter
    def description(self, value):
        update_request = pb.FeatureStringFieldUpdateRequest()
        update_request.new_value = value
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureDescription(update_request)
        self._refresh()

    @property
    def classifiers(self):
        return set(self._internal_feature.classifiers)

    @classifiers.setter
    def classifiers(self, value: set):
        update_request = pb.FeatureStringArrayFieldUpdateRequest()
        update_request.new_value[:] = list(value)
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureClassifiers(update_request)
        self._refresh()

    @property
    def importance(self):
        return self._internal_feature.importance

    @importance.setter
    def importance(self, value):
        update_request = pb.FeatureDoubleFieldUpdateRequest()
        update_request.new_value = value
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureImportance(update_request)
        self._refresh()

    @property
    def monitoring(self):
        return Monitoring(self._stub, self._fs, self)

    @property
    def special_data(self):
        return FeatureSpecialData(self)

    @property
    def custom_data(self):
        return self._internal_feature.custom_data

    @custom_data.setter
    def custom_data(self, value):
        update_request = pb.FeatureCustomDataUpdateRequest()
        update_request.new_value.CopyFrom(value)
        update_request.absolute_feature_name = self._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureCustomData(update_request)
        self._refresh()

    @property
    def nested_features(self):
        return {
            feature.name: Feature(
                self._stub,
                self._fs,
                feature,
                self._absolute_feature_name + "." + feature.name,
            )
            for feature in self._internal_feature.nested_features
        }

    def _reference(self) -> FeatureRef:
        return FeatureRef(self._absolute_feature_name, self._fs._reference())

    def __lt__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.LT, value)

    def __le__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.LE, value)

    def __gt__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.GT, value)

    def __ge__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.GE, value)

    def __eq__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.EQ, value)

    def __ne__(self, value: str) -> query.FilterCondition:
        return query.FilterCondition(self._reference(), query.FilterOperator.NE, value)

    def _refresh(self):
        self._fs.refresh()
        feature_name_segments = self._absolute_feature_name.split(".")
        output_feature = [
            f
            for f in self._fs._feature_set.features
            if f.name == feature_name_segments[0]
        ][0]
        for segment in feature_name_segments[1:]:
            output_feature = [
                f for f in output_feature.nested_features if f.name == segment
            ][0]
        self._internal_feature = output_feature

    def __repr__(self):
        return Utils.pretty_print_proto(self._internal_feature)


class FeatureProfile:
    def __init__(self, stub, feature_set, feature):
        self._stub = stub
        self._fs = feature_set
        self._feature = feature

    @property
    def feature_type(self):
        return FeatureSetApi.FeatureTypeInternal.FeatureType.Name(
            self._feature._internal_feature.profile.feature_type
        )

    @feature_type.setter
    def feature_type(self, value):
        valid_values = FeatureSetApi.FeatureType.keys()
        if value.upper() in valid_values:
            update_request = pb.FeatureTypeUpdateRequest()
            update_request.new_value = FeatureSetApi.FeatureType.Value(value.upper())
            update_request.absolute_feature_name = self._feature._absolute_feature_name
            update_request.header.CopyFrom(self._fs._feature_set_header)
            self._stub.UpdateFeatureType(update_request)
            self._feature._refresh()
        else:
            raise Exception(
                "Invalid feature type. Supported values are: "
                + ", ".join(map(str, valid_values))
            )

    @property
    def categorical_statistics(self):
        return CategoricalStatistics(self._feature._internal_feature)

    @property
    def statistics(self):
        return FeatureStatistics(self._feature._internal_feature)

    def __repr__(self):
        return Utils.pretty_print_proto(self._feature._internal_feature.profile)


class FeatureStatistics:
    def __init__(self, feature):
        self._feature = feature
        self._stats = self._feature.categorical

    @property
    def max(self):
        return self._stats.max

    @property
    def mean(self):
        return self._stats.mean

    @property
    def median(self):
        return self._stats.median

    @property
    def min(self):
        return self._stats.min

    @property
    def stddev(self):
        return self._stats.stddev

    @property
    def stddev_rec_count(self):
        return self._stats.stddev_rec_count

    @property
    def null_count(self):
        return self._stats.null_count

    @property
    def nan_count(self):
        return self._stats.nan_count

    @property
    def unique(self):
        return self._stats.unique

    def __repr__(self):
        return Utils.pretty_print_proto(self._stats)


class CategoricalStatistics:
    def __init__(self, feature):
        self._feature = feature
        self._categorical = self._feature.categorical

    @property
    def unique(self):
        return self._categorical.unique

    @property
    def top(self):
        return [FeatureTop(top) for top in self._categorical.top]

    def __repr__(self):
        return Utils.pretty_print_proto(self._categorical)


class FeatureTop:
    def __init__(self, feature):
        self._feature = feature
        self._top = self._feature.top

    @property
    def name(self):
        return self._top.name

    @property
    def count(self):
        return self._top.count

    def __repr__(self):
        return Utils.pretty_print_proto(self._top)


class Monitoring:
    def __init__(self, stub, feature_set, feature):
        self._stub = stub
        self._fs = feature_set
        self._feature = feature

    @property
    def anomaly_detection(self):
        return self._feature._internal_feature.monitoring.anomaly_detection

    @anomaly_detection.setter
    def anomaly_detection(self, value):
        update_request = pb.FeatureBooleanFieldUpdateRequest()
        update_request.new_value = value
        update_request.absolute_feature_name = self._feature._absolute_feature_name
        update_request.header.CopyFrom(self._fs._feature_set_header)
        self._stub.UpdateFeatureAnomalyDetection(update_request)
        self._feature._refresh()

    def __repr__(self):
        return Utils.pretty_print_proto(self._feature._internal_feature.monitoring)


class FeatureSpecialData:
    def __init__(self, feature):
        self._feature = feature

    @property
    def spi(self):
        return self._feature._internal_feature.special_data.spi

    @property
    def pci(self):
        return self._feature._internal_feature.special_data.pci

    @property
    def rpi(self):
        return self._feature._internal_feature.special_data.rpi

    @property
    def demographic(self):
        return self._feature._internal_feature.special_data.demographic

    @property
    def sensitive(self):
        return self._feature._internal_feature.special_data.sensitive

    def __repr__(self):
        return Utils.pretty_print_proto(self._feature._internal_feature.special_data)
