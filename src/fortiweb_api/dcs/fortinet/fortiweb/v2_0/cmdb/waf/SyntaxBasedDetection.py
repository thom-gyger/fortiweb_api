from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SyntaxBasedDetection(EndpointBase):
    from .SyntaxBasedDetectionExceptionItem import SyntaxBasedDetectionExceptionItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    detection_target_sql: str = field(metadata=EndpointBase.post_mark)
    detection_target_xss: str= field(metadata=EndpointBase.post_mark)
    sql_detection_template: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_status: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_action: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_block_period: int= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_severity: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_trigger: str= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_id: int= field(metadata=EndpointBase.post_mark)
    xss_html_tag_based_check_level: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_status: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_action: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_block_period: int= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_severity: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_trigger: str= field(metadata=EndpointBase.post_mark)
    xss_html_attribute_based_id: int= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_status: str= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_action: str= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_block_period: int= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_severity: str= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_trigger: str= field(metadata=EndpointBase.post_mark)
    xss_html_css_based_id: int= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_status: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_action: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_block_period: int= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_severity: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_trigger: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_function_based_id: int= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_status: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_action: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_block_period: int= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_severity: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_trigger: str= field(metadata=EndpointBase.post_mark)
    xss_javascript_variable_based_id: int= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_status: str= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_action: str= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_severity: str= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_stacked_queries_id: int= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_status: str= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_action: str= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_severity: str= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_embeded_queries_id: int= field(metadata=EndpointBase.post_mark)
    sql_condition_based_status: str= field(metadata=EndpointBase.post_mark)
    sql_condition_based_action: str= field(metadata=EndpointBase.post_mark)
    sql_condition_based_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_condition_based_severity: str= field(metadata=EndpointBase.post_mark)
    sql_condition_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_condition_based_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_condition_based_id: int= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_status: str= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_action: str= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_severity: str= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_arithmetic_operation_id: int= field(metadata=EndpointBase.post_mark)
    sql_line_comments_status: str= field(metadata=EndpointBase.post_mark)
    sql_line_comments_action: str= field(metadata=EndpointBase.post_mark)
    sql_line_comments_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_line_comments_severity: str= field(metadata=EndpointBase.post_mark)
    sql_line_comments_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_line_comments_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_line_comments_id: int= field(metadata=EndpointBase.post_mark)
    sql_function_based_status: str= field(metadata=EndpointBase.post_mark)
    sql_function_based_action: str= field(metadata=EndpointBase.post_mark)
    sql_function_based_block_period: int= field(metadata=EndpointBase.post_mark)
    sql_function_based_severity: str= field(metadata=EndpointBase.post_mark)
    sql_function_based_threat_weight: str= field(metadata=EndpointBase.post_mark)
    sql_function_based_trigger: str= field(metadata=EndpointBase.post_mark)
    sql_function_based_id: int= field(metadata=EndpointBase.post_mark)
    sz_exception_element_list: int

    exception_element_list: Optional[List[SyntaxBasedDetectionExceptionItem]]
    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()