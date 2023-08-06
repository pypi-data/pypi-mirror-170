from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_queue_response_200_item_raw_flow_failure_module_value_type_2_iterator_type_0 import (
    ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0,
)
from ..models.list_queue_response_200_item_raw_flow_failure_module_value_type_2_iterator_type_1 import (
    ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType1,
)
from ..models.list_queue_response_200_item_raw_flow_failure_module_value_type_2_type import (
    ListQueueResponse200ItemRawFlowFailureModuleValueType2Type,
)

T = TypeVar("T", bound="ListQueueResponse200ItemRawFlowFailureModuleValueType2")


@attr.s(auto_attribs=True)
class ListQueueResponse200ItemRawFlowFailureModuleValueType2:
    """ """

    iterator: Union[
        ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0,
        ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType1,
    ]
    skip_failures: bool
    type: ListQueueResponse200ItemRawFlowFailureModuleValueType2Type
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.iterator, ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0):
            iterator = self.iterator.to_dict()

        else:
            iterator = self.iterator.to_dict()

        skip_failures = self.skip_failures
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iterator": iterator,
                "skip_failures": skip_failures,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_iterator(
            data: object,
        ) -> Union[
            ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0,
            ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType1,
        ]:
            try:
                iterator_type_0: ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0
                if not isinstance(data, dict):
                    raise TypeError()
                iterator_type_0 = ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType0.from_dict(data)

                return iterator_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            iterator_type_1: ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType1
            iterator_type_1 = ListQueueResponse200ItemRawFlowFailureModuleValueType2IteratorType1.from_dict(data)

            return iterator_type_1

        iterator = _parse_iterator(d.pop("iterator"))

        skip_failures = d.pop("skip_failures")

        type = ListQueueResponse200ItemRawFlowFailureModuleValueType2Type(d.pop("type"))

        list_queue_response_200_item_raw_flow_failure_module_value_type_2 = cls(
            iterator=iterator,
            skip_failures=skip_failures,
            type=type,
        )

        list_queue_response_200_item_raw_flow_failure_module_value_type_2.additional_properties = d
        return list_queue_response_200_item_raw_flow_failure_module_value_type_2

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
