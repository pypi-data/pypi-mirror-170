from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.queued_job_raw_flow_modules_item_input_transforms import QueuedJobRawFlowModulesItemInputTransforms
from ..models.queued_job_raw_flow_modules_item_retry import QueuedJobRawFlowModulesItemRetry
from ..models.queued_job_raw_flow_modules_item_sleep_type_0 import QueuedJobRawFlowModulesItemSleepType0
from ..models.queued_job_raw_flow_modules_item_sleep_type_1 import QueuedJobRawFlowModulesItemSleepType1
from ..models.queued_job_raw_flow_modules_item_stop_after_if import QueuedJobRawFlowModulesItemStopAfterIf
from ..models.queued_job_raw_flow_modules_item_value_type_0 import QueuedJobRawFlowModulesItemValueType0
from ..models.queued_job_raw_flow_modules_item_value_type_1 import QueuedJobRawFlowModulesItemValueType1
from ..models.queued_job_raw_flow_modules_item_value_type_2 import QueuedJobRawFlowModulesItemValueType2
from ..models.queued_job_raw_flow_modules_item_value_type_3 import QueuedJobRawFlowModulesItemValueType3
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueuedJobRawFlowModulesItem")


@attr.s(auto_attribs=True)
class QueuedJobRawFlowModulesItem:
    """ """

    input_transforms: QueuedJobRawFlowModulesItemInputTransforms
    value: Union[
        QueuedJobRawFlowModulesItemValueType0,
        QueuedJobRawFlowModulesItemValueType1,
        QueuedJobRawFlowModulesItemValueType2,
        QueuedJobRawFlowModulesItemValueType3,
    ]
    stop_after_if: Union[Unset, QueuedJobRawFlowModulesItemStopAfterIf] = UNSET
    sleep: Union[QueuedJobRawFlowModulesItemSleepType0, QueuedJobRawFlowModulesItemSleepType1, Unset] = UNSET
    summary: Union[Unset, str] = UNSET
    suspend: Union[Unset, int] = UNSET
    retry: Union[Unset, QueuedJobRawFlowModulesItemRetry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_transforms = self.input_transforms.to_dict()

        if isinstance(self.value, QueuedJobRawFlowModulesItemValueType0):
            value = self.value.to_dict()

        elif isinstance(self.value, QueuedJobRawFlowModulesItemValueType1):
            value = self.value.to_dict()

        elif isinstance(self.value, QueuedJobRawFlowModulesItemValueType2):
            value = self.value.to_dict()

        else:
            value = self.value.to_dict()

        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET
        elif isinstance(self.sleep, QueuedJobRawFlowModulesItemSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        summary = self.summary
        suspend = self.suspend
        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_transforms": input_transforms,
                "value": value,
            }
        )
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if summary is not UNSET:
            field_dict["summary"] = summary
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_transforms = QueuedJobRawFlowModulesItemInputTransforms.from_dict(d.pop("input_transforms"))

        def _parse_value(
            data: object,
        ) -> Union[
            QueuedJobRawFlowModulesItemValueType0,
            QueuedJobRawFlowModulesItemValueType1,
            QueuedJobRawFlowModulesItemValueType2,
            QueuedJobRawFlowModulesItemValueType3,
        ]:
            try:
                value_type_0: QueuedJobRawFlowModulesItemValueType0
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = QueuedJobRawFlowModulesItemValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            try:
                value_type_1: QueuedJobRawFlowModulesItemValueType1
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = QueuedJobRawFlowModulesItemValueType1.from_dict(data)

                return value_type_1
            except:  # noqa: E722
                pass
            try:
                value_type_2: QueuedJobRawFlowModulesItemValueType2
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = QueuedJobRawFlowModulesItemValueType2.from_dict(data)

                return value_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            value_type_3: QueuedJobRawFlowModulesItemValueType3
            value_type_3 = QueuedJobRawFlowModulesItemValueType3.from_dict(data)

            return value_type_3

        value = _parse_value(d.pop("value"))

        stop_after_if: Union[Unset, QueuedJobRawFlowModulesItemStopAfterIf] = UNSET
        _stop_after_if = d.pop("stop_after_if", UNSET)
        if not isinstance(_stop_after_if, Unset):
            stop_after_if = QueuedJobRawFlowModulesItemStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[QueuedJobRawFlowModulesItemSleepType0, QueuedJobRawFlowModulesItemSleepType1, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                sleep_type_0: Union[Unset, QueuedJobRawFlowModulesItemSleepType0]
                if not isinstance(data, dict):
                    raise TypeError()
                sleep_type_0 = UNSET
                _sleep_type_0 = data
                if not isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = QueuedJobRawFlowModulesItemSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            sleep_type_1: Union[Unset, QueuedJobRawFlowModulesItemSleepType1]
            sleep_type_1 = UNSET
            _sleep_type_1 = data
            if not isinstance(_sleep_type_1, Unset):
                sleep_type_1 = QueuedJobRawFlowModulesItemSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        summary = d.pop("summary", UNSET)

        suspend = d.pop("suspend", UNSET)

        retry: Union[Unset, QueuedJobRawFlowModulesItemRetry] = UNSET
        _retry = d.pop("retry", UNSET)
        if not isinstance(_retry, Unset):
            retry = QueuedJobRawFlowModulesItemRetry.from_dict(_retry)

        queued_job_raw_flow_modules_item = cls(
            input_transforms=input_transforms,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            summary=summary,
            suspend=suspend,
            retry=retry,
        )

        queued_job_raw_flow_modules_item.additional_properties = d
        return queued_job_raw_flow_modules_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
