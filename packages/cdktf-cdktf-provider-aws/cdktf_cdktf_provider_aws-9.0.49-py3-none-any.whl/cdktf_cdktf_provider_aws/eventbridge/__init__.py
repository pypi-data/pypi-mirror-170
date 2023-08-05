import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class CloudwatchEventApiDestination(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventApiDestination",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination aws_cloudwatch_event_api_destination}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        connection_arn: builtins.str,
        http_method: builtins.str,
        invocation_endpoint: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        invocation_rate_limit_per_second: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination aws_cloudwatch_event_api_destination} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#connection_arn CloudwatchEventApiDestination#connection_arn}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#http_method CloudwatchEventApiDestination#http_method}.
        :param invocation_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_endpoint CloudwatchEventApiDestination#invocation_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#name CloudwatchEventApiDestination#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#description CloudwatchEventApiDestination#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#id CloudwatchEventApiDestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param invocation_rate_limit_per_second: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_rate_limit_per_second CloudwatchEventApiDestination#invocation_rate_limit_per_second}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventApiDestination.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventApiDestinationConfig(
            connection_arn=connection_arn,
            http_method=http_method,
            invocation_endpoint=invocation_endpoint,
            name=name,
            description=description,
            id=id,
            invocation_rate_limit_per_second=invocation_rate_limit_per_second,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInvocationRateLimitPerSecond")
    def reset_invocation_rate_limit_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationRateLimitPerSecond", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="connectionArnInput")
    def connection_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="invocationEndpointInput")
    def invocation_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invocationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="invocationRateLimitPerSecondInput")
    def invocation_rate_limit_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "invocationRateLimitPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "connection_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="invocationEndpoint")
    def invocation_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invocationEndpoint"))

    @invocation_endpoint.setter
    def invocation_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "invocation_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invocationEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="invocationRateLimitPerSecond")
    def invocation_rate_limit_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "invocationRateLimitPerSecond"))

    @invocation_rate_limit_per_second.setter
    def invocation_rate_limit_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "invocation_rate_limit_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invocationRateLimitPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventApiDestination, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventApiDestinationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_arn": "connectionArn",
        "http_method": "httpMethod",
        "invocation_endpoint": "invocationEndpoint",
        "name": "name",
        "description": "description",
        "id": "id",
        "invocation_rate_limit_per_second": "invocationRateLimitPerSecond",
    },
)
class CloudwatchEventApiDestinationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        connection_arn: builtins.str,
        http_method: builtins.str,
        invocation_endpoint: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        invocation_rate_limit_per_second: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#connection_arn CloudwatchEventApiDestination#connection_arn}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#http_method CloudwatchEventApiDestination#http_method}.
        :param invocation_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_endpoint CloudwatchEventApiDestination#invocation_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#name CloudwatchEventApiDestination#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#description CloudwatchEventApiDestination#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#id CloudwatchEventApiDestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param invocation_rate_limit_per_second: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_rate_limit_per_second CloudwatchEventApiDestination#invocation_rate_limit_per_second}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventApiDestinationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument invocation_endpoint", value=invocation_endpoint, expected_type=type_hints["invocation_endpoint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument invocation_rate_limit_per_second", value=invocation_rate_limit_per_second, expected_type=type_hints["invocation_rate_limit_per_second"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_arn": connection_arn,
            "http_method": http_method,
            "invocation_endpoint": invocation_endpoint,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if invocation_rate_limit_per_second is not None:
            self._values["invocation_rate_limit_per_second"] = invocation_rate_limit_per_second

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#connection_arn CloudwatchEventApiDestination#connection_arn}.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#http_method CloudwatchEventApiDestination#http_method}.'''
        result = self._values.get("http_method")
        assert result is not None, "Required property 'http_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_endpoint CloudwatchEventApiDestination#invocation_endpoint}.'''
        result = self._values.get("invocation_endpoint")
        assert result is not None, "Required property 'invocation_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#name CloudwatchEventApiDestination#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#description CloudwatchEventApiDestination#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#id CloudwatchEventApiDestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invocation_rate_limit_per_second(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_api_destination#invocation_rate_limit_per_second CloudwatchEventApiDestination#invocation_rate_limit_per_second}.'''
        result = self._values.get("invocation_rate_limit_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventApiDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventArchive(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventArchive",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive aws_cloudwatch_event_archive}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        event_source_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive aws_cloudwatch_event_archive} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param event_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_source_arn CloudwatchEventArchive#event_source_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#name CloudwatchEventArchive#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#description CloudwatchEventArchive#description}.
        :param event_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_pattern CloudwatchEventArchive#event_pattern}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#id CloudwatchEventArchive#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#retention_days CloudwatchEventArchive#retention_days}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventArchive.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventArchiveConfig(
            event_source_arn=event_source_arn,
            name=name,
            description=description,
            event_pattern=event_pattern,
            id=id,
            retention_days=retention_days,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEventPattern")
    def reset_event_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventPattern", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventPatternInput")
    def event_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceArnInput")
    def event_source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventSourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventPattern"))

    @event_pattern.setter
    def event_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "event_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventPattern", value)

    @builtins.property
    @jsii.member(jsii_name="eventSourceArn")
    def event_source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventSourceArn"))

    @event_source_arn.setter
    def event_source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "event_source_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventArchive, "retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventArchiveConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "event_source_arn": "eventSourceArn",
        "name": "name",
        "description": "description",
        "event_pattern": "eventPattern",
        "id": "id",
        "retention_days": "retentionDays",
    },
)
class CloudwatchEventArchiveConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        event_source_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param event_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_source_arn CloudwatchEventArchive#event_source_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#name CloudwatchEventArchive#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#description CloudwatchEventArchive#description}.
        :param event_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_pattern CloudwatchEventArchive#event_pattern}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#id CloudwatchEventArchive#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#retention_days CloudwatchEventArchive#retention_days}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventArchiveConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument event_source_arn", value=event_source_arn, expected_type=type_hints["event_source_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_source_arn": event_source_arn,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern
        if id is not None:
            self._values["id"] = id
        if retention_days is not None:
            self._values["retention_days"] = retention_days

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def event_source_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_source_arn CloudwatchEventArchive#event_source_arn}.'''
        result = self._values.get("event_source_arn")
        assert result is not None, "Required property 'event_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#name CloudwatchEventArchive#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#description CloudwatchEventArchive#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#event_pattern CloudwatchEventArchive#event_pattern}.'''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#id CloudwatchEventArchive#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_archive#retention_days CloudwatchEventArchive#retention_days}.'''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventArchiveConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventBus(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventBus",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus aws_cloudwatch_event_bus}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        event_source_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus aws_cloudwatch_event_bus} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#name CloudwatchEventBus#name}.
        :param event_source_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#event_source_name CloudwatchEventBus#event_source_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#id CloudwatchEventBus#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags CloudwatchEventBus#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags_all CloudwatchEventBus#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventBus.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventBusConfig(
            name=name,
            event_source_name=event_source_name,
            id=id,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEventSourceName")
    def reset_event_source_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSourceName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceNameInput")
    def event_source_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventSourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceName")
    def event_source_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventSourceName"))

    @event_source_name.setter
    def event_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBus, "event_source_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBus, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBus, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBus, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBus, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventBusConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "event_source_name": "eventSourceName",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CloudwatchEventBusConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        name: builtins.str,
        event_source_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#name CloudwatchEventBus#name}.
        :param event_source_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#event_source_name CloudwatchEventBus#event_source_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#id CloudwatchEventBus#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags CloudwatchEventBus#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags_all CloudwatchEventBus#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventBusConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument event_source_name", value=event_source_name, expected_type=type_hints["event_source_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if event_source_name is not None:
            self._values["event_source_name"] = event_source_name
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#name CloudwatchEventBus#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_source_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#event_source_name CloudwatchEventBus#event_source_name}.'''
        result = self._values.get("event_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#id CloudwatchEventBus#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags CloudwatchEventBus#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus#tags_all CloudwatchEventBus#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventBusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventBusPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventBusPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy aws_cloudwatch_event_bus_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        policy: builtins.str,
        event_bus_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy aws_cloudwatch_event_bus_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#policy CloudwatchEventBusPolicy#policy}.
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#event_bus_name CloudwatchEventBusPolicy#event_bus_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#id CloudwatchEventBusPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventBusPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventBusPolicyConfig(
            policy=policy,
            event_bus_name=event_bus_name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEventBusName")
    def reset_event_bus_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBusName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="eventBusNameInput")
    def event_bus_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventBusNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBusName")
    def event_bus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventBusName"))

    @event_bus_name.setter
    def event_bus_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBusPolicy, "event_bus_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBusPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventBusPolicy, "policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventBusPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "policy": "policy",
        "event_bus_name": "eventBusName",
        "id": "id",
    },
)
class CloudwatchEventBusPolicyConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        policy: builtins.str,
        event_bus_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#policy CloudwatchEventBusPolicy#policy}.
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#event_bus_name CloudwatchEventBusPolicy#event_bus_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#id CloudwatchEventBusPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventBusPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#policy CloudwatchEventBusPolicy#policy}.'''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#event_bus_name CloudwatchEventBusPolicy#event_bus_name}.'''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_bus_policy#id CloudwatchEventBusPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventBusPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection aws_cloudwatch_event_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        authorization_type: builtins.str,
        auth_parameters: typing.Union["CloudwatchEventConnectionAuthParameters", typing.Dict[str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection aws_cloudwatch_event_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_type CloudwatchEventConnection#authorization_type}.
        :param auth_parameters: auth_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#auth_parameters CloudwatchEventConnection#auth_parameters}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#name CloudwatchEventConnection#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#description CloudwatchEventConnection#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#id CloudwatchEventConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventConnectionConfig(
            authorization_type=authorization_type,
            auth_parameters=auth_parameters,
            name=name,
            description=description,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthParameters")
    def put_auth_parameters(
        self,
        *,
        api_key: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersApiKey", typing.Dict[str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersBasic", typing.Dict[str, typing.Any]]] = None,
        invocation_http_parameters: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParameters", typing.Dict[str, typing.Any]]] = None,
        oauth: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersOauth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#api_key CloudwatchEventConnection#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#basic CloudwatchEventConnection#basic}
        :param invocation_http_parameters: invocation_http_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#invocation_http_parameters CloudwatchEventConnection#invocation_http_parameters}
        :param oauth: oauth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth CloudwatchEventConnection#oauth}
        '''
        value = CloudwatchEventConnectionAuthParameters(
            api_key=api_key,
            basic=basic,
            invocation_http_parameters=invocation_http_parameters,
            oauth=oauth,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthParameters", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="authParameters")
    def auth_parameters(
        self,
    ) -> "CloudwatchEventConnectionAuthParametersOutputReference":
        return typing.cast("CloudwatchEventConnectionAuthParametersOutputReference", jsii.get(self, "authParameters"))

    @builtins.property
    @jsii.member(jsii_name="secretArn")
    def secret_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretArn"))

    @builtins.property
    @jsii.member(jsii_name="authorizationTypeInput")
    def authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authParametersInput")
    def auth_parameters_input(
        self,
    ) -> typing.Optional["CloudwatchEventConnectionAuthParameters"]:
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParameters"], jsii.get(self, "authParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationType"))

    @authorization_type.setter
    def authorization_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnection, "authorization_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnection, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParameters",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "basic": "basic",
        "invocation_http_parameters": "invocationHttpParameters",
        "oauth": "oauth",
    },
)
class CloudwatchEventConnectionAuthParameters:
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersApiKey", typing.Dict[str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersBasic", typing.Dict[str, typing.Any]]] = None,
        invocation_http_parameters: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParameters", typing.Dict[str, typing.Any]]] = None,
        oauth: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersOauth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#api_key CloudwatchEventConnection#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#basic CloudwatchEventConnection#basic}
        :param invocation_http_parameters: invocation_http_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#invocation_http_parameters CloudwatchEventConnection#invocation_http_parameters}
        :param oauth: oauth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth CloudwatchEventConnection#oauth}
        '''
        if isinstance(api_key, dict):
            api_key = CloudwatchEventConnectionAuthParametersApiKey(**api_key)
        if isinstance(basic, dict):
            basic = CloudwatchEventConnectionAuthParametersBasic(**basic)
        if isinstance(invocation_http_parameters, dict):
            invocation_http_parameters = CloudwatchEventConnectionAuthParametersInvocationHttpParameters(**invocation_http_parameters)
        if isinstance(oauth, dict):
            oauth = CloudwatchEventConnectionAuthParametersOauth(**oauth)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParameters.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
            check_type(argname="argument invocation_http_parameters", value=invocation_http_parameters, expected_type=type_hints["invocation_http_parameters"])
            check_type(argname="argument oauth", value=oauth, expected_type=type_hints["oauth"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_key is not None:
            self._values["api_key"] = api_key
        if basic is not None:
            self._values["basic"] = basic
        if invocation_http_parameters is not None:
            self._values["invocation_http_parameters"] = invocation_http_parameters
        if oauth is not None:
            self._values["oauth"] = oauth

    @builtins.property
    def api_key(
        self,
    ) -> typing.Optional["CloudwatchEventConnectionAuthParametersApiKey"]:
        '''api_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#api_key CloudwatchEventConnection#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParametersApiKey"], result)

    @builtins.property
    def basic(self) -> typing.Optional["CloudwatchEventConnectionAuthParametersBasic"]:
        '''basic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#basic CloudwatchEventConnection#basic}
        '''
        result = self._values.get("basic")
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParametersBasic"], result)

    @builtins.property
    def invocation_http_parameters(
        self,
    ) -> typing.Optional["CloudwatchEventConnectionAuthParametersInvocationHttpParameters"]:
        '''invocation_http_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#invocation_http_parameters CloudwatchEventConnection#invocation_http_parameters}
        '''
        result = self._values.get("invocation_http_parameters")
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParametersInvocationHttpParameters"], result)

    @builtins.property
    def oauth(self) -> typing.Optional["CloudwatchEventConnectionAuthParametersOauth"]:
        '''oauth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth CloudwatchEventConnection#oauth}
        '''
        result = self._values.get("oauth")
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParametersOauth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersApiKey",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersApiKey:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersApiKey.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersApiKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersApiKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersApiKeyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersApiKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersApiKeyOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersApiKeyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersApiKey]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersApiKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersApiKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersApiKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersBasic",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class CloudwatchEventConnectionAuthParametersBasic:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#password CloudwatchEventConnection#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#username CloudwatchEventConnection#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersBasic.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#password CloudwatchEventConnection#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#username CloudwatchEventConnection#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersBasic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersBasicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersBasicOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersBasicOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersBasicOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersBasicOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersBasic]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersBasic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersBasic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersBasicOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParameters",
    jsii_struct_bases=[],
    name_mapping={"body": "body", "header": "header", "query_string": "queryString"},
)
class CloudwatchEventConnectionAuthParametersInvocationHttpParameters:
    def __init__(
        self,
        *,
        body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody", typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader", typing.Dict[str, typing.Any]]]]] = None,
        query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParameters.__init__)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body is not None:
            self._values["body"] = body
        if header is not None:
            self._values["header"] = header
        if query_string is not None:
            self._values["query_string"] = query_string

    @builtins.property
    def body(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody"]]]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody"]]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader"]]], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString"]]]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersInvocationHttpParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBody")
    def put_body(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference.put_body)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference.put_query_string)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList:
        return typing.cast(CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList:
        return typing.cast(CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList":
        return typing.cast("CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody]]], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString"]]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersInvocationHttpParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersInvocationHttpParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersInvocationHttpParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauth",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_endpoint": "authorizationEndpoint",
        "http_method": "httpMethod",
        "oauth_http_parameters": "oauthHttpParameters",
        "client_parameters": "clientParameters",
    },
)
class CloudwatchEventConnectionAuthParametersOauth:
    def __init__(
        self,
        *,
        authorization_endpoint: builtins.str,
        http_method: builtins.str,
        oauth_http_parameters: typing.Union["CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters", typing.Dict[str, typing.Any]],
        client_parameters: typing.Optional[typing.Union["CloudwatchEventConnectionAuthParametersOauthClientParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_endpoint CloudwatchEventConnection#authorization_endpoint}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#http_method CloudwatchEventConnection#http_method}.
        :param oauth_http_parameters: oauth_http_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth_http_parameters CloudwatchEventConnection#oauth_http_parameters}
        :param client_parameters: client_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_parameters CloudwatchEventConnection#client_parameters}
        '''
        if isinstance(oauth_http_parameters, dict):
            oauth_http_parameters = CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters(**oauth_http_parameters)
        if isinstance(client_parameters, dict):
            client_parameters = CloudwatchEventConnectionAuthParametersOauthClientParameters(**client_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauth.__init__)
            check_type(argname="argument authorization_endpoint", value=authorization_endpoint, expected_type=type_hints["authorization_endpoint"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument oauth_http_parameters", value=oauth_http_parameters, expected_type=type_hints["oauth_http_parameters"])
            check_type(argname="argument client_parameters", value=client_parameters, expected_type=type_hints["client_parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_endpoint": authorization_endpoint,
            "http_method": http_method,
            "oauth_http_parameters": oauth_http_parameters,
        }
        if client_parameters is not None:
            self._values["client_parameters"] = client_parameters

    @builtins.property
    def authorization_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_endpoint CloudwatchEventConnection#authorization_endpoint}.'''
        result = self._values.get("authorization_endpoint")
        assert result is not None, "Required property 'authorization_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#http_method CloudwatchEventConnection#http_method}.'''
        result = self._values.get("http_method")
        assert result is not None, "Required property 'http_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_http_parameters(
        self,
    ) -> "CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters":
        '''oauth_http_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth_http_parameters CloudwatchEventConnection#oauth_http_parameters}
        '''
        result = self._values.get("oauth_http_parameters")
        assert result is not None, "Required property 'oauth_http_parameters' is missing"
        return typing.cast("CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters", result)

    @builtins.property
    def client_parameters(
        self,
    ) -> typing.Optional["CloudwatchEventConnectionAuthParametersOauthClientParameters"]:
        '''client_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_parameters CloudwatchEventConnection#client_parameters}
        '''
        result = self._values.get("client_parameters")
        return typing.cast(typing.Optional["CloudwatchEventConnectionAuthParametersOauthClientParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthClientParameters",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId", "client_secret": "clientSecret"},
)
class CloudwatchEventConnectionAuthParametersOauthClientParameters:
    def __init__(self, *, client_id: builtins.str, client_secret: builtins.str) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_id CloudwatchEventConnection#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_secret CloudwatchEventConnection#client_secret}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthClientParameters.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_id CloudwatchEventConnection#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_secret CloudwatchEventConnection#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauthClientParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauthClientParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauthClientParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersOauthClientParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters",
    jsii_struct_bases=[],
    name_mapping={"body": "body", "header": "header", "query_string": "queryString"},
)
class CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters:
    def __init__(
        self,
        *,
        body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody", typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader", typing.Dict[str, typing.Any]]]]] = None,
        query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters.__init__)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body is not None:
            self._values["body"] = body
        if header is not None:
            self._values["header"] = header
        if query_string is not None:
            self._values["query_string"] = query_string

    @builtins.property
    def body(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody"]]]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody"]]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader"]]], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString"]]]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBody")
    def put_body(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference.put_body)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference.put_query_string)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(
        self,
    ) -> CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList:
        return typing.cast(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList:
        return typing.cast(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList":
        return typing.cast("CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody]]], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString"]]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString",
    jsii_struct_bases=[],
    name_mapping={"is_value_secret": "isValueSecret", "key": "key", "value": "value"},
)
class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString:
    def __init__(
        self,
        *,
        is_value_secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param is_value_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString.__init__)
            check_type(argname="argument is_value_secret", value=is_value_secret, expected_type=type_hints["is_value_secret"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_value_secret is not None:
            self._values["is_value_secret"] = is_value_secret
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def is_value_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#is_value_secret CloudwatchEventConnection#is_value_secret}.'''
        result = self._values.get("is_value_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsValueSecret")
    def reset_is_value_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsValueSecret", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="isValueSecretInput")
    def is_value_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isValueSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="isValueSecret")
    def is_value_secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isValueSecret"))

    @is_value_secret.setter
    def is_value_secret(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference, "is_value_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isValueSecret", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOauthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOauthOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOauthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientParameters")
    def put_client_parameters(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_id CloudwatchEventConnection#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_secret CloudwatchEventConnection#client_secret}.
        '''
        value = CloudwatchEventConnectionAuthParametersOauthClientParameters(
            client_id=client_id, client_secret=client_secret
        )

        return typing.cast(None, jsii.invoke(self, "putClientParameters", [value]))

    @jsii.member(jsii_name="putOauthHttpParameters")
    def put_oauth_http_parameters(
        self,
        *,
        body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody, typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader, typing.Dict[str, typing.Any]]]]] = None,
        query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        value = CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters(
            body=body, header=header, query_string=query_string
        )

        return typing.cast(None, jsii.invoke(self, "putOauthHttpParameters", [value]))

    @jsii.member(jsii_name="resetClientParameters")
    def reset_client_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientParameters", []))

    @builtins.property
    @jsii.member(jsii_name="clientParameters")
    def client_parameters(
        self,
    ) -> CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference, jsii.get(self, "clientParameters"))

    @builtins.property
    @jsii.member(jsii_name="oauthHttpParameters")
    def oauth_http_parameters(
        self,
    ) -> CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference, jsii.get(self, "oauthHttpParameters"))

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpointInput")
    def authorization_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="clientParametersInput")
    def client_parameters_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauthClientParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauthClientParameters], jsii.get(self, "clientParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthHttpParametersInput")
    def oauth_http_parameters_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters], jsii.get(self, "oauthHttpParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpoint")
    def authorization_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationEndpoint"))

    @authorization_endpoint.setter
    def authorization_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOutputReference, "authorization_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOutputReference, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauth]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParametersOauth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOauthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventConnectionAuthParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionAuthParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionAuthParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApiKey")
    def put_api_key(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#key CloudwatchEventConnection#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#value CloudwatchEventConnection#value}.
        '''
        value_ = CloudwatchEventConnectionAuthParametersApiKey(key=key, value=value)

        return typing.cast(None, jsii.invoke(self, "putApiKey", [value_]))

    @jsii.member(jsii_name="putBasic")
    def put_basic(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#password CloudwatchEventConnection#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#username CloudwatchEventConnection#username}.
        '''
        value = CloudwatchEventConnectionAuthParametersBasic(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasic", [value]))

    @jsii.member(jsii_name="putInvocationHttpParameters")
    def put_invocation_http_parameters(
        self,
        *,
        body: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody, typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader, typing.Dict[str, typing.Any]]]]] = None,
        query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#body CloudwatchEventConnection#body}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#header CloudwatchEventConnection#header}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#query_string CloudwatchEventConnection#query_string}
        '''
        value = CloudwatchEventConnectionAuthParametersInvocationHttpParameters(
            body=body, header=header, query_string=query_string
        )

        return typing.cast(None, jsii.invoke(self, "putInvocationHttpParameters", [value]))

    @jsii.member(jsii_name="putOauth")
    def put_oauth(
        self,
        *,
        authorization_endpoint: builtins.str,
        http_method: builtins.str,
        oauth_http_parameters: typing.Union[CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters, typing.Dict[str, typing.Any]],
        client_parameters: typing.Optional[typing.Union[CloudwatchEventConnectionAuthParametersOauthClientParameters, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_endpoint CloudwatchEventConnection#authorization_endpoint}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#http_method CloudwatchEventConnection#http_method}.
        :param oauth_http_parameters: oauth_http_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#oauth_http_parameters CloudwatchEventConnection#oauth_http_parameters}
        :param client_parameters: client_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#client_parameters CloudwatchEventConnection#client_parameters}
        '''
        value = CloudwatchEventConnectionAuthParametersOauth(
            authorization_endpoint=authorization_endpoint,
            http_method=http_method,
            oauth_http_parameters=oauth_http_parameters,
            client_parameters=client_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putOauth", [value]))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetBasic")
    def reset_basic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasic", []))

    @jsii.member(jsii_name="resetInvocationHttpParameters")
    def reset_invocation_http_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationHttpParameters", []))

    @jsii.member(jsii_name="resetOauth")
    def reset_oauth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth", []))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> CloudwatchEventConnectionAuthParametersApiKeyOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersApiKeyOutputReference, jsii.get(self, "apiKey"))

    @builtins.property
    @jsii.member(jsii_name="basic")
    def basic(self) -> CloudwatchEventConnectionAuthParametersBasicOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersBasicOutputReference, jsii.get(self, "basic"))

    @builtins.property
    @jsii.member(jsii_name="invocationHttpParameters")
    def invocation_http_parameters(
        self,
    ) -> CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference, jsii.get(self, "invocationHttpParameters"))

    @builtins.property
    @jsii.member(jsii_name="oauth")
    def oauth(self) -> CloudwatchEventConnectionAuthParametersOauthOutputReference:
        return typing.cast(CloudwatchEventConnectionAuthParametersOauthOutputReference, jsii.get(self, "oauth"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersApiKey]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersApiKey], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="basicInput")
    def basic_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersBasic]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersBasic], jsii.get(self, "basicInput"))

    @builtins.property
    @jsii.member(jsii_name="invocationHttpParametersInput")
    def invocation_http_parameters_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersInvocationHttpParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersInvocationHttpParameters], jsii.get(self, "invocationHttpParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthInput")
    def oauth_input(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParametersOauth]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParametersOauth], jsii.get(self, "oauthInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventConnectionAuthParameters]:
        return typing.cast(typing.Optional[CloudwatchEventConnectionAuthParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventConnectionAuthParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventConnectionAuthParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authorization_type": "authorizationType",
        "auth_parameters": "authParameters",
        "name": "name",
        "description": "description",
        "id": "id",
    },
)
class CloudwatchEventConnectionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        authorization_type: builtins.str,
        auth_parameters: typing.Union[CloudwatchEventConnectionAuthParameters, typing.Dict[str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_type CloudwatchEventConnection#authorization_type}.
        :param auth_parameters: auth_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#auth_parameters CloudwatchEventConnection#auth_parameters}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#name CloudwatchEventConnection#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#description CloudwatchEventConnection#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#id CloudwatchEventConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auth_parameters, dict):
            auth_parameters = CloudwatchEventConnectionAuthParameters(**auth_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument auth_parameters", value=auth_parameters, expected_type=type_hints["auth_parameters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_type": authorization_type,
            "auth_parameters": auth_parameters,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def authorization_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#authorization_type CloudwatchEventConnection#authorization_type}.'''
        result = self._values.get("authorization_type")
        assert result is not None, "Required property 'authorization_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_parameters(self) -> CloudwatchEventConnectionAuthParameters:
        '''auth_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#auth_parameters CloudwatchEventConnection#auth_parameters}
        '''
        result = self._values.get("auth_parameters")
        assert result is not None, "Required property 'auth_parameters' is missing"
        return typing.cast(CloudwatchEventConnectionAuthParameters, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#name CloudwatchEventConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#description CloudwatchEventConnection#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_connection#id CloudwatchEventConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventPermission(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventPermission",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission aws_cloudwatch_event_permission}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        principal: builtins.str,
        statement_id: builtins.str,
        action: typing.Optional[builtins.str] = None,
        condition: typing.Optional[typing.Union["CloudwatchEventPermissionCondition", typing.Dict[str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission aws_cloudwatch_event_permission} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#principal CloudwatchEventPermission#principal}.
        :param statement_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#statement_id CloudwatchEventPermission#statement_id}.
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#action CloudwatchEventPermission#action}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#condition CloudwatchEventPermission#condition}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#event_bus_name CloudwatchEventPermission#event_bus_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#id CloudwatchEventPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventPermission.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventPermissionConfig(
            principal=principal,
            statement_id=statement_id,
            action=action,
            condition=condition,
            event_bus_name=event_bus_name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        key: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#key CloudwatchEventPermission#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#type CloudwatchEventPermission#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#value CloudwatchEventPermission#value}.
        '''
        value_ = CloudwatchEventPermissionCondition(key=key, type=type, value=value)

        return typing.cast(None, jsii.invoke(self, "putCondition", [value_]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetEventBusName")
    def reset_event_bus_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBusName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> "CloudwatchEventPermissionConditionOutputReference":
        return typing.cast("CloudwatchEventPermissionConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional["CloudwatchEventPermissionCondition"]:
        return typing.cast(typing.Optional["CloudwatchEventPermissionCondition"], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBusNameInput")
    def event_bus_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventBusNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="statementIdInput")
    def statement_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermission, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="eventBusName")
    def event_bus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventBusName"))

    @event_bus_name.setter
    def event_bus_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermission, "event_bus_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermission, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermission, "principal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementId"))

    @statement_id.setter
    def statement_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermission, "statement_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventPermissionCondition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CloudwatchEventPermissionCondition:
    def __init__(
        self,
        *,
        key: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#key CloudwatchEventPermission#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#type CloudwatchEventPermission#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#value CloudwatchEventPermission#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventPermissionCondition.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "type": type,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#key CloudwatchEventPermission#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#type CloudwatchEventPermission#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#value CloudwatchEventPermission#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventPermissionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventPermissionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventPermissionConditionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventPermissionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermissionConditionOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermissionConditionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermissionConditionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventPermissionCondition]:
        return typing.cast(typing.Optional[CloudwatchEventPermissionCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventPermissionCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventPermissionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventPermissionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "principal": "principal",
        "statement_id": "statementId",
        "action": "action",
        "condition": "condition",
        "event_bus_name": "eventBusName",
        "id": "id",
    },
)
class CloudwatchEventPermissionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        principal: builtins.str,
        statement_id: builtins.str,
        action: typing.Optional[builtins.str] = None,
        condition: typing.Optional[typing.Union[CloudwatchEventPermissionCondition, typing.Dict[str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#principal CloudwatchEventPermission#principal}.
        :param statement_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#statement_id CloudwatchEventPermission#statement_id}.
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#action CloudwatchEventPermission#action}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#condition CloudwatchEventPermission#condition}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#event_bus_name CloudwatchEventPermission#event_bus_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#id CloudwatchEventPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = CloudwatchEventPermissionCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventPermissionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "principal": principal,
            "statement_id": statement_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if action is not None:
            self._values["action"] = action
        if condition is not None:
            self._values["condition"] = condition
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#principal CloudwatchEventPermission#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#statement_id CloudwatchEventPermission#statement_id}.'''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#action CloudwatchEventPermission#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def condition(self) -> typing.Optional[CloudwatchEventPermissionCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#condition CloudwatchEventPermission#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[CloudwatchEventPermissionCondition], result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#event_bus_name CloudwatchEventPermission#event_bus_name}.'''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission#id CloudwatchEventPermission#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventPermissionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule aws_cloudwatch_event_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule aws_cloudwatch_event_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#description CloudwatchEventRule#description}.
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_bus_name CloudwatchEventRule#event_bus_name}.
        :param event_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_pattern CloudwatchEventRule#event_pattern}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#id CloudwatchEventRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#is_enabled CloudwatchEventRule#is_enabled}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name CloudwatchEventRule#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name_prefix CloudwatchEventRule#name_prefix}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#role_arn CloudwatchEventRule#role_arn}.
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#schedule_expression CloudwatchEventRule#schedule_expression}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags CloudwatchEventRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags_all CloudwatchEventRule#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventRuleConfig(
            description=description,
            event_bus_name=event_bus_name,
            event_pattern=event_pattern,
            id=id,
            is_enabled=is_enabled,
            name=name,
            name_prefix=name_prefix,
            role_arn=role_arn,
            schedule_expression=schedule_expression,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEventBusName")
    def reset_event_bus_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBusName", []))

    @jsii.member(jsii_name="resetEventPattern")
    def reset_event_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventPattern", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsEnabled")
    def reset_is_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsEnabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetScheduleExpression")
    def reset_schedule_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleExpression", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBusNameInput")
    def event_bus_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventBusNameInput"))

    @builtins.property
    @jsii.member(jsii_name="eventPatternInput")
    def event_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionInput")
    def schedule_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventBusName")
    def event_bus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventBusName"))

    @event_bus_name.setter
    def event_bus_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "event_bus_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusName", value)

    @builtins.property
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventPattern"))

    @event_pattern.setter
    def event_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "event_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventPattern", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "schedule_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventRule, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "event_bus_name": "eventBusName",
        "event_pattern": "eventPattern",
        "id": "id",
        "is_enabled": "isEnabled",
        "name": "name",
        "name_prefix": "namePrefix",
        "role_arn": "roleArn",
        "schedule_expression": "scheduleExpression",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CloudwatchEventRuleConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#description CloudwatchEventRule#description}.
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_bus_name CloudwatchEventRule#event_bus_name}.
        :param event_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_pattern CloudwatchEventRule#event_pattern}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#id CloudwatchEventRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#is_enabled CloudwatchEventRule#is_enabled}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name CloudwatchEventRule#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name_prefix CloudwatchEventRule#name_prefix}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#role_arn CloudwatchEventRule#role_arn}.
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#schedule_expression CloudwatchEventRule#schedule_expression}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags CloudwatchEventRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags_all CloudwatchEventRule#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern
        if id is not None:
            self._values["id"] = id
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#description CloudwatchEventRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_bus_name CloudwatchEventRule#event_bus_name}.'''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#event_pattern CloudwatchEventRule#event_pattern}.'''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#id CloudwatchEventRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#is_enabled CloudwatchEventRule#is_enabled}.'''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name CloudwatchEventRule#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#name_prefix CloudwatchEventRule#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#role_arn CloudwatchEventRule#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#schedule_expression CloudwatchEventRule#schedule_expression}.'''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags CloudwatchEventRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule#tags_all CloudwatchEventRule#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTarget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTarget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target aws_cloudwatch_event_target}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        arn: builtins.str,
        rule: builtins.str,
        batch_target: typing.Optional[typing.Union["CloudwatchEventTargetBatchTarget", typing.Dict[str, typing.Any]]] = None,
        dead_letter_config: typing.Optional[typing.Union["CloudwatchEventTargetDeadLetterConfig", typing.Dict[str, typing.Any]]] = None,
        ecs_target: typing.Optional[typing.Union["CloudwatchEventTargetEcsTarget", typing.Dict[str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudwatchEventTargetHttpTarget", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        input_transformer: typing.Optional[typing.Union["CloudwatchEventTargetInputTransformer", typing.Dict[str, typing.Any]]] = None,
        kinesis_target: typing.Optional[typing.Union["CloudwatchEventTargetKinesisTarget", typing.Dict[str, typing.Any]]] = None,
        redshift_target: typing.Optional[typing.Union["CloudwatchEventTargetRedshiftTarget", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["CloudwatchEventTargetRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        run_command_targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[str, typing.Any]]]]] = None,
        sqs_target: typing.Optional[typing.Union["CloudwatchEventTargetSqsTarget", typing.Dict[str, typing.Any]]] = None,
        target_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target aws_cloudwatch_event_target} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.
        :param batch_target: batch_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        :param ecs_target: ecs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.
        :param input_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.
        :param input_transformer: input_transformer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        :param kinesis_target: kinesis_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        :param redshift_target: redshift_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.
        :param run_command_targets: run_command_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        :param sqs_target: sqs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTarget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventTargetConfig(
            arn=arn,
            rule=rule,
            batch_target=batch_target,
            dead_letter_config=dead_letter_config,
            ecs_target=ecs_target,
            event_bus_name=event_bus_name,
            http_target=http_target,
            id=id,
            input=input,
            input_path=input_path,
            input_transformer=input_transformer,
            kinesis_target=kinesis_target,
            redshift_target=redshift_target,
            retry_policy=retry_policy,
            role_arn=role_arn,
            run_command_targets=run_command_targets,
            sqs_target=sqs_target,
            target_id=target_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBatchTarget")
    def put_batch_target(
        self,
        *,
        job_definition: builtins.str,
        job_name: builtins.str,
        array_size: typing.Optional[jsii.Number] = None,
        job_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.
        :param job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.
        :param array_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.
        :param job_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.
        '''
        value = CloudwatchEventTargetBatchTarget(
            job_definition=job_definition,
            job_name=job_name,
            array_size=array_size,
            job_attempts=job_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putBatchTarget", [value]))

    @jsii.member(jsii_name="putDeadLetterConfig")
    def put_dead_letter_config(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        '''
        value = CloudwatchEventTargetDeadLetterConfig(arn=arn)

        return typing.cast(None, jsii.invoke(self, "putDeadLetterConfig", [value]))

    @jsii.member(jsii_name="putEcsTarget")
    def put_ecs_target(
        self,
        *,
        task_definition_arn: builtins.str,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["CloudwatchEventTargetEcsTargetNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        placement_constraint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param task_definition_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        :param placement_constraint: placement_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.
        '''
        value = CloudwatchEventTargetEcsTarget(
            task_definition_arn=task_definition_arn,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            group=group,
            launch_type=launch_type,
            network_configuration=network_configuration,
            placement_constraint=placement_constraint,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            tags=tags,
            task_count=task_count,
        )

        return typing.cast(None, jsii.invoke(self, "putEcsTarget", [value]))

    @jsii.member(jsii_name="putHttpTarget")
    def put_http_target(
        self,
        *,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param header_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.
        :param path_parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.
        '''
        value = CloudwatchEventTargetHttpTarget(
            header_parameters=header_parameters,
            path_parameter_values=path_parameter_values,
            query_string_parameters=query_string_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpTarget", [value]))

    @jsii.member(jsii_name="putInputTransformer")
    def put_input_transformer(
        self,
        *,
        input_template: builtins.str,
        input_paths: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param input_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.
        :param input_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.
        '''
        value = CloudwatchEventTargetInputTransformer(
            input_template=input_template, input_paths=input_paths
        )

        return typing.cast(None, jsii.invoke(self, "putInputTransformer", [value]))

    @jsii.member(jsii_name="putKinesisTarget")
    def put_kinesis_target(
        self,
        *,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.
        '''
        value = CloudwatchEventTargetKinesisTarget(
            partition_key_path=partition_key_path
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisTarget", [value]))

    @jsii.member(jsii_name="putRedshiftTarget")
    def put_redshift_target(
        self,
        *,
        database: builtins.str,
        db_user: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        sql: typing.Optional[builtins.str] = None,
        statement_name: typing.Optional[builtins.str] = None,
        with_event: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.
        :param db_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.
        :param statement_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.
        :param with_event: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.
        '''
        value = CloudwatchEventTargetRedshiftTarget(
            database=database,
            db_user=db_user,
            secrets_manager_arn=secrets_manager_arn,
            sql=sql,
            statement_name=statement_name,
            with_event=with_event,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftTarget", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.
        '''
        value = CloudwatchEventTargetRetryPolicy(
            maximum_event_age_in_seconds=maximum_event_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putRunCommandTargets")
    def put_run_command_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTarget.put_run_command_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRunCommandTargets", [value]))

    @jsii.member(jsii_name="putSqsTarget")
    def put_sqs_target(
        self,
        *,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.
        '''
        value = CloudwatchEventTargetSqsTarget(message_group_id=message_group_id)

        return typing.cast(None, jsii.invoke(self, "putSqsTarget", [value]))

    @jsii.member(jsii_name="resetBatchTarget")
    def reset_batch_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchTarget", []))

    @jsii.member(jsii_name="resetDeadLetterConfig")
    def reset_dead_letter_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterConfig", []))

    @jsii.member(jsii_name="resetEcsTarget")
    def reset_ecs_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEcsTarget", []))

    @jsii.member(jsii_name="resetEventBusName")
    def reset_event_bus_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBusName", []))

    @jsii.member(jsii_name="resetHttpTarget")
    def reset_http_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTarget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetInputPath")
    def reset_input_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputPath", []))

    @jsii.member(jsii_name="resetInputTransformer")
    def reset_input_transformer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputTransformer", []))

    @jsii.member(jsii_name="resetKinesisTarget")
    def reset_kinesis_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisTarget", []))

    @jsii.member(jsii_name="resetRedshiftTarget")
    def reset_redshift_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftTarget", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetRunCommandTargets")
    def reset_run_command_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommandTargets", []))

    @jsii.member(jsii_name="resetSqsTarget")
    def reset_sqs_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqsTarget", []))

    @jsii.member(jsii_name="resetTargetId")
    def reset_target_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="batchTarget")
    def batch_target(self) -> "CloudwatchEventTargetBatchTargetOutputReference":
        return typing.cast("CloudwatchEventTargetBatchTargetOutputReference", jsii.get(self, "batchTarget"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> "CloudwatchEventTargetDeadLetterConfigOutputReference":
        return typing.cast("CloudwatchEventTargetDeadLetterConfigOutputReference", jsii.get(self, "deadLetterConfig"))

    @builtins.property
    @jsii.member(jsii_name="ecsTarget")
    def ecs_target(self) -> "CloudwatchEventTargetEcsTargetOutputReference":
        return typing.cast("CloudwatchEventTargetEcsTargetOutputReference", jsii.get(self, "ecsTarget"))

    @builtins.property
    @jsii.member(jsii_name="httpTarget")
    def http_target(self) -> "CloudwatchEventTargetHttpTargetOutputReference":
        return typing.cast("CloudwatchEventTargetHttpTargetOutputReference", jsii.get(self, "httpTarget"))

    @builtins.property
    @jsii.member(jsii_name="inputTransformer")
    def input_transformer(
        self,
    ) -> "CloudwatchEventTargetInputTransformerOutputReference":
        return typing.cast("CloudwatchEventTargetInputTransformerOutputReference", jsii.get(self, "inputTransformer"))

    @builtins.property
    @jsii.member(jsii_name="kinesisTarget")
    def kinesis_target(self) -> "CloudwatchEventTargetKinesisTargetOutputReference":
        return typing.cast("CloudwatchEventTargetKinesisTargetOutputReference", jsii.get(self, "kinesisTarget"))

    @builtins.property
    @jsii.member(jsii_name="redshiftTarget")
    def redshift_target(self) -> "CloudwatchEventTargetRedshiftTargetOutputReference":
        return typing.cast("CloudwatchEventTargetRedshiftTargetOutputReference", jsii.get(self, "redshiftTarget"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "CloudwatchEventTargetRetryPolicyOutputReference":
        return typing.cast("CloudwatchEventTargetRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="runCommandTargets")
    def run_command_targets(self) -> "CloudwatchEventTargetRunCommandTargetsList":
        return typing.cast("CloudwatchEventTargetRunCommandTargetsList", jsii.get(self, "runCommandTargets"))

    @builtins.property
    @jsii.member(jsii_name="sqsTarget")
    def sqs_target(self) -> "CloudwatchEventTargetSqsTargetOutputReference":
        return typing.cast("CloudwatchEventTargetSqsTargetOutputReference", jsii.get(self, "sqsTarget"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="batchTargetInput")
    def batch_target_input(self) -> typing.Optional["CloudwatchEventTargetBatchTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetBatchTarget"], jsii.get(self, "batchTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterConfigInput")
    def dead_letter_config_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetDeadLetterConfig"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetDeadLetterConfig"], jsii.get(self, "deadLetterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="ecsTargetInput")
    def ecs_target_input(self) -> typing.Optional["CloudwatchEventTargetEcsTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTarget"], jsii.get(self, "ecsTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBusNameInput")
    def event_bus_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventBusNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTargetInput")
    def http_target_input(self) -> typing.Optional["CloudwatchEventTargetHttpTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetHttpTarget"], jsii.get(self, "httpTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="inputPathInput")
    def input_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="inputTransformerInput")
    def input_transformer_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetInputTransformer"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetInputTransformer"], jsii.get(self, "inputTransformerInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisTargetInput")
    def kinesis_target_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetKinesisTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetKinesisTarget"], jsii.get(self, "kinesisTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftTargetInput")
    def redshift_target_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetRedshiftTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetRedshiftTarget"], jsii.get(self, "redshiftTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(self) -> typing.Optional["CloudwatchEventTargetRetryPolicy"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandTargetsInput")
    def run_command_targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]], jsii.get(self, "runCommandTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsTargetInput")
    def sqs_target_input(self) -> typing.Optional["CloudwatchEventTargetSqsTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetSqsTarget"], jsii.get(self, "sqsTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIdInput")
    def target_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="eventBusName")
    def event_bus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventBusName"))

    @event_bus_name.setter
    def event_bus_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "event_bus_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "input"))

    @input.setter
    def input(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "input").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "input", value)

    @builtins.property
    @jsii.member(jsii_name="inputPath")
    def input_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputPath"))

    @input_path.setter
    def input_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "input_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputPath", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTarget, "target_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetBatchTarget",
    jsii_struct_bases=[],
    name_mapping={
        "job_definition": "jobDefinition",
        "job_name": "jobName",
        "array_size": "arraySize",
        "job_attempts": "jobAttempts",
    },
)
class CloudwatchEventTargetBatchTarget:
    def __init__(
        self,
        *,
        job_definition: builtins.str,
        job_name: builtins.str,
        array_size: typing.Optional[jsii.Number] = None,
        job_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.
        :param job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.
        :param array_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.
        :param job_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetBatchTarget.__init__)
            check_type(argname="argument job_definition", value=job_definition, expected_type=type_hints["job_definition"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument array_size", value=array_size, expected_type=type_hints["array_size"])
            check_type(argname="argument job_attempts", value=job_attempts, expected_type=type_hints["job_attempts"])
        self._values: typing.Dict[str, typing.Any] = {
            "job_definition": job_definition,
            "job_name": job_name,
        }
        if array_size is not None:
            self._values["array_size"] = array_size
        if job_attempts is not None:
            self._values["job_attempts"] = job_attempts

    @builtins.property
    def job_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.'''
        result = self._values.get("job_definition")
        assert result is not None, "Required property 'job_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.'''
        result = self._values.get("job_name")
        assert result is not None, "Required property 'job_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def array_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.'''
        result = self._values.get("array_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def job_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.'''
        result = self._values.get("job_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetBatchTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetBatchTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetBatchTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetBatchTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArraySize")
    def reset_array_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArraySize", []))

    @jsii.member(jsii_name="resetJobAttempts")
    def reset_job_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobAttempts", []))

    @builtins.property
    @jsii.member(jsii_name="arraySizeInput")
    def array_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "arraySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="jobAttemptsInput")
    def job_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jobAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="jobDefinitionInput")
    def job_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="jobNameInput")
    def job_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobNameInput"))

    @builtins.property
    @jsii.member(jsii_name="arraySize")
    def array_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "arraySize"))

    @array_size.setter
    def array_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetBatchTargetOutputReference, "array_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arraySize", value)

    @builtins.property
    @jsii.member(jsii_name="jobAttempts")
    def job_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jobAttempts"))

    @job_attempts.setter
    def job_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetBatchTargetOutputReference, "job_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="jobDefinition")
    def job_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobDefinition"))

    @job_definition.setter
    def job_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetBatchTargetOutputReference, "job_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetBatchTargetOutputReference, "job_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetBatchTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetBatchTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetBatchTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetBatchTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "arn": "arn",
        "rule": "rule",
        "batch_target": "batchTarget",
        "dead_letter_config": "deadLetterConfig",
        "ecs_target": "ecsTarget",
        "event_bus_name": "eventBusName",
        "http_target": "httpTarget",
        "id": "id",
        "input": "input",
        "input_path": "inputPath",
        "input_transformer": "inputTransformer",
        "kinesis_target": "kinesisTarget",
        "redshift_target": "redshiftTarget",
        "retry_policy": "retryPolicy",
        "role_arn": "roleArn",
        "run_command_targets": "runCommandTargets",
        "sqs_target": "sqsTarget",
        "target_id": "targetId",
    },
)
class CloudwatchEventTargetConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        arn: builtins.str,
        rule: builtins.str,
        batch_target: typing.Optional[typing.Union[CloudwatchEventTargetBatchTarget, typing.Dict[str, typing.Any]]] = None,
        dead_letter_config: typing.Optional[typing.Union["CloudwatchEventTargetDeadLetterConfig", typing.Dict[str, typing.Any]]] = None,
        ecs_target: typing.Optional[typing.Union["CloudwatchEventTargetEcsTarget", typing.Dict[str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudwatchEventTargetHttpTarget", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        input_transformer: typing.Optional[typing.Union["CloudwatchEventTargetInputTransformer", typing.Dict[str, typing.Any]]] = None,
        kinesis_target: typing.Optional[typing.Union["CloudwatchEventTargetKinesisTarget", typing.Dict[str, typing.Any]]] = None,
        redshift_target: typing.Optional[typing.Union["CloudwatchEventTargetRedshiftTarget", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["CloudwatchEventTargetRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        run_command_targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[str, typing.Any]]]]] = None,
        sqs_target: typing.Optional[typing.Union["CloudwatchEventTargetSqsTarget", typing.Dict[str, typing.Any]]] = None,
        target_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.
        :param batch_target: batch_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        :param ecs_target: ecs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.
        :param input_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.
        :param input_transformer: input_transformer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        :param kinesis_target: kinesis_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        :param redshift_target: redshift_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.
        :param run_command_targets: run_command_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        :param sqs_target: sqs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(batch_target, dict):
            batch_target = CloudwatchEventTargetBatchTarget(**batch_target)
        if isinstance(dead_letter_config, dict):
            dead_letter_config = CloudwatchEventTargetDeadLetterConfig(**dead_letter_config)
        if isinstance(ecs_target, dict):
            ecs_target = CloudwatchEventTargetEcsTarget(**ecs_target)
        if isinstance(http_target, dict):
            http_target = CloudwatchEventTargetHttpTarget(**http_target)
        if isinstance(input_transformer, dict):
            input_transformer = CloudwatchEventTargetInputTransformer(**input_transformer)
        if isinstance(kinesis_target, dict):
            kinesis_target = CloudwatchEventTargetKinesisTarget(**kinesis_target)
        if isinstance(redshift_target, dict):
            redshift_target = CloudwatchEventTargetRedshiftTarget(**redshift_target)
        if isinstance(retry_policy, dict):
            retry_policy = CloudwatchEventTargetRetryPolicy(**retry_policy)
        if isinstance(sqs_target, dict):
            sqs_target = CloudwatchEventTargetSqsTarget(**sqs_target)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument batch_target", value=batch_target, expected_type=type_hints["batch_target"])
            check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
            check_type(argname="argument ecs_target", value=ecs_target, expected_type=type_hints["ecs_target"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument http_target", value=http_target, expected_type=type_hints["http_target"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument input_transformer", value=input_transformer, expected_type=type_hints["input_transformer"])
            check_type(argname="argument kinesis_target", value=kinesis_target, expected_type=type_hints["kinesis_target"])
            check_type(argname="argument redshift_target", value=redshift_target, expected_type=type_hints["redshift_target"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument run_command_targets", value=run_command_targets, expected_type=type_hints["run_command_targets"])
            check_type(argname="argument sqs_target", value=sqs_target, expected_type=type_hints["sqs_target"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "rule": rule,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if batch_target is not None:
            self._values["batch_target"] = batch_target
        if dead_letter_config is not None:
            self._values["dead_letter_config"] = dead_letter_config
        if ecs_target is not None:
            self._values["ecs_target"] = ecs_target
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if http_target is not None:
            self._values["http_target"] = http_target
        if id is not None:
            self._values["id"] = id
        if input is not None:
            self._values["input"] = input
        if input_path is not None:
            self._values["input_path"] = input_path
        if input_transformer is not None:
            self._values["input_transformer"] = input_transformer
        if kinesis_target is not None:
            self._values["kinesis_target"] = kinesis_target
        if redshift_target is not None:
            self._values["redshift_target"] = redshift_target
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if run_command_targets is not None:
            self._values["run_command_targets"] = run_command_targets
        if sqs_target is not None:
            self._values["sqs_target"] = sqs_target
        if target_id is not None:
            self._values["target_id"] = target_id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_target(self) -> typing.Optional[CloudwatchEventTargetBatchTarget]:
        '''batch_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        '''
        result = self._values.get("batch_target")
        return typing.cast(typing.Optional[CloudwatchEventTargetBatchTarget], result)

    @builtins.property
    def dead_letter_config(
        self,
    ) -> typing.Optional["CloudwatchEventTargetDeadLetterConfig"]:
        '''dead_letter_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        '''
        result = self._values.get("dead_letter_config")
        return typing.cast(typing.Optional["CloudwatchEventTargetDeadLetterConfig"], result)

    @builtins.property
    def ecs_target(self) -> typing.Optional["CloudwatchEventTargetEcsTarget"]:
        '''ecs_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        '''
        result = self._values.get("ecs_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTarget"], result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.'''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_target(self) -> typing.Optional["CloudwatchEventTargetHttpTarget"]:
        '''http_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        '''
        result = self._values.get("http_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetHttpTarget"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.'''
        result = self._values.get("input")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.'''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_transformer(
        self,
    ) -> typing.Optional["CloudwatchEventTargetInputTransformer"]:
        '''input_transformer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        '''
        result = self._values.get("input_transformer")
        return typing.cast(typing.Optional["CloudwatchEventTargetInputTransformer"], result)

    @builtins.property
    def kinesis_target(self) -> typing.Optional["CloudwatchEventTargetKinesisTarget"]:
        '''kinesis_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        '''
        result = self._values.get("kinesis_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetKinesisTarget"], result)

    @builtins.property
    def redshift_target(self) -> typing.Optional["CloudwatchEventTargetRedshiftTarget"]:
        '''redshift_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        '''
        result = self._values.get("redshift_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetRedshiftTarget"], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["CloudwatchEventTargetRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["CloudwatchEventTargetRetryPolicy"], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_command_targets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]]:
        '''run_command_targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        '''
        result = self._values.get("run_command_targets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]], result)

    @builtins.property
    def sqs_target(self) -> typing.Optional["CloudwatchEventTargetSqsTarget"]:
        '''sqs_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        '''
        result = self._values.get("sqs_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetSqsTarget"], result)

    @builtins.property
    def target_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.'''
        result = self._values.get("target_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetDeadLetterConfig",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class CloudwatchEventTargetDeadLetterConfig:
    def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetDeadLetterConfig.__init__)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetDeadLetterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetDeadLetterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetDeadLetterConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetDeadLetterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetDeadLetterConfigOutputReference, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetDeadLetterConfig]:
        return typing.cast(typing.Optional[CloudwatchEventTargetDeadLetterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetDeadLetterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetDeadLetterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "task_definition_arn": "taskDefinitionArn",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "group": "group",
        "launch_type": "launchType",
        "network_configuration": "networkConfiguration",
        "placement_constraint": "placementConstraint",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "tags": "tags",
        "task_count": "taskCount",
    },
)
class CloudwatchEventTargetEcsTarget:
    def __init__(
        self,
        *,
        task_definition_arn: builtins.str,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["CloudwatchEventTargetEcsTargetNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        placement_constraint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param task_definition_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        :param placement_constraint: placement_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.
        '''
        if isinstance(network_configuration, dict):
            network_configuration = CloudwatchEventTargetEcsTargetNetworkConfiguration(**network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTarget.__init__)
            check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument placement_constraint", value=placement_constraint, expected_type=type_hints["placement_constraint"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_definition_arn": task_definition_arn,
        }
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if group is not None:
            self._values["group"] = group
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if placement_constraint is not None:
            self._values["placement_constraint"] = placement_constraint
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count

    @builtins.property
    def task_definition_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.'''
        result = self._values.get("task_definition_arn")
        assert result is not None, "Required property 'task_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.'''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_execute_command(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.'''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["CloudwatchEventTargetEcsTargetNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTargetNetworkConfiguration"], result)

    @builtins.property
    def placement_constraint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]]:
        '''placement_constraint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        '''
        result = self._values.get("placement_constraint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.'''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class CloudwatchEventTargetEcsTargetNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetNetworkConfiguration.__init__)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnets": subnets,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTargetNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, "subnets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetEcsTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.
        '''
        value = CloudwatchEventTargetEcsTargetNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putPlacementConstraint")
    def put_placement_constraint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetOutputReference.put_placement_constraint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraint", [value]))

    @jsii.member(jsii_name="resetEnableEcsManagedTags")
    def reset_enable_ecs_managed_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEcsManagedTags", []))

    @jsii.member(jsii_name="resetEnableExecuteCommand")
    def reset_enable_execute_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExecuteCommand", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetPlacementConstraint")
    def reset_placement_constraint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraint", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaskCount")
    def reset_task_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskCount", []))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference:
        return typing.cast(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraint")
    def placement_constraint(
        self,
    ) -> "CloudwatchEventTargetEcsTargetPlacementConstraintList":
        return typing.cast("CloudwatchEventTargetEcsTargetPlacementConstraintList", jsii.get(self, "placementConstraint"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTagsInput")
    def enable_ecs_managed_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableEcsManagedTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommandInput")
    def enable_execute_command_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableExecuteCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintInput")
    def placement_constraint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]], jsii.get(self, "placementConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskCountInput")
    def task_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskCountInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArnInput")
    def task_definition_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableEcsManagedTags"))

    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "enable_ecs_managed_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEcsManagedTags", value)

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommand")
    def enable_execute_command(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableExecuteCommand"))

    @enable_execute_command.setter
    def enable_execute_command(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "enable_execute_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExecuteCommand", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "launch_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "platform_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "propagate_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="taskCount")
    def task_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskCount"))

    @task_count.setter
    def task_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "task_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskCount", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArn")
    def task_definition_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinitionArn"))

    @task_definition_arn.setter
    def task_definition_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "task_definition_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinitionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetEcsTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetEcsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetPlacementConstraint",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class CloudwatchEventTargetEcsTargetPlacementConstraint:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#type CloudwatchEventTarget#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#expression CloudwatchEventTarget#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetPlacementConstraint.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#type CloudwatchEventTarget#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#expression CloudwatchEventTarget#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTargetPlacementConstraint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetEcsTargetPlacementConstraintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetPlacementConstraintList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetPlacementConstraintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetPlacementConstraintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetHttpTarget",
    jsii_struct_bases=[],
    name_mapping={
        "header_parameters": "headerParameters",
        "path_parameter_values": "pathParameterValues",
        "query_string_parameters": "queryStringParameters",
    },
)
class CloudwatchEventTargetHttpTarget:
    def __init__(
        self,
        *,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param header_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.
        :param path_parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetHttpTarget.__init__)
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.'''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.'''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.'''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetHttpTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetHttpTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetHttpTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetHttpTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHeaderParameters")
    def reset_header_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderParameters", []))

    @jsii.member(jsii_name="resetPathParameterValues")
    def reset_path_parameter_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathParameterValues", []))

    @jsii.member(jsii_name="resetQueryStringParameters")
    def reset_query_string_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringParameters", []))

    @builtins.property
    @jsii.member(jsii_name="headerParametersInput")
    def header_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headerParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="pathParameterValuesInput")
    def path_parameter_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathParameterValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringParametersInput")
    def query_string_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "queryStringParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="headerParameters")
    def header_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headerParameters"))

    @header_parameters.setter
    def header_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetHttpTargetOutputReference, "header_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerParameters", value)

    @builtins.property
    @jsii.member(jsii_name="pathParameterValues")
    def path_parameter_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathParameterValues"))

    @path_parameter_values.setter
    def path_parameter_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetHttpTargetOutputReference, "path_parameter_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathParameterValues", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringParameters")
    def query_string_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "queryStringParameters"))

    @query_string_parameters.setter
    def query_string_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetHttpTargetOutputReference, "query_string_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringParameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetHttpTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetHttpTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetHttpTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetHttpTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetInputTransformer",
    jsii_struct_bases=[],
    name_mapping={"input_template": "inputTemplate", "input_paths": "inputPaths"},
)
class CloudwatchEventTargetInputTransformer:
    def __init__(
        self,
        *,
        input_template: builtins.str,
        input_paths: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param input_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.
        :param input_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetInputTransformer.__init__)
            check_type(argname="argument input_template", value=input_template, expected_type=type_hints["input_template"])
            check_type(argname="argument input_paths", value=input_paths, expected_type=type_hints["input_paths"])
        self._values: typing.Dict[str, typing.Any] = {
            "input_template": input_template,
        }
        if input_paths is not None:
            self._values["input_paths"] = input_paths

    @builtins.property
    def input_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.'''
        result = self._values.get("input_template")
        assert result is not None, "Required property 'input_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_paths(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.'''
        result = self._values.get("input_paths")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetInputTransformer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetInputTransformerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetInputTransformerOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetInputTransformerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInputPaths")
    def reset_input_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputPaths", []))

    @builtins.property
    @jsii.member(jsii_name="inputPathsInput")
    def input_paths_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "inputPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="inputTemplateInput")
    def input_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="inputPaths")
    def input_paths(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "inputPaths"))

    @input_paths.setter
    def input_paths(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetInputTransformerOutputReference, "input_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputPaths", value)

    @builtins.property
    @jsii.member(jsii_name="inputTemplate")
    def input_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputTemplate"))

    @input_template.setter
    def input_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetInputTransformerOutputReference, "input_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetInputTransformer]:
        return typing.cast(typing.Optional[CloudwatchEventTargetInputTransformer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetInputTransformer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetInputTransformerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetKinesisTarget",
    jsii_struct_bases=[],
    name_mapping={"partition_key_path": "partitionKeyPath"},
)
class CloudwatchEventTargetKinesisTarget:
    def __init__(
        self,
        *,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetKinesisTarget.__init__)
            check_type(argname="argument partition_key_path", value=partition_key_path, expected_type=type_hints["partition_key_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if partition_key_path is not None:
            self._values["partition_key_path"] = partition_key_path

    @builtins.property
    def partition_key_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.'''
        result = self._values.get("partition_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetKinesisTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetKinesisTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetKinesisTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetKinesisTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPartitionKeyPath")
    def reset_partition_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKeyPath", []))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPathInput")
    def partition_key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPath")
    def partition_key_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKeyPath"))

    @partition_key_path.setter
    def partition_key_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetKinesisTargetOutputReference, "partition_key_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetKinesisTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetKinesisTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetKinesisTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetKinesisTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRedshiftTarget",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "db_user": "dbUser",
        "secrets_manager_arn": "secretsManagerArn",
        "sql": "sql",
        "statement_name": "statementName",
        "with_event": "withEvent",
    },
)
class CloudwatchEventTargetRedshiftTarget:
    def __init__(
        self,
        *,
        database: builtins.str,
        db_user: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        sql: typing.Optional[builtins.str] = None,
        statement_name: typing.Optional[builtins.str] = None,
        with_event: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.
        :param db_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.
        :param statement_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.
        :param with_event: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRedshiftTarget.__init__)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument db_user", value=db_user, expected_type=type_hints["db_user"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument statement_name", value=statement_name, expected_type=type_hints["statement_name"])
            check_type(argname="argument with_event", value=with_event, expected_type=type_hints["with_event"])
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
        }
        if db_user is not None:
            self._values["db_user"] = db_user
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if sql is not None:
            self._values["sql"] = sql
        if statement_name is not None:
            self._values["statement_name"] = statement_name
        if with_event is not None:
            self._values["with_event"] = with_event

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.'''
        result = self._values.get("db_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.'''
        result = self._values.get("sql")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.'''
        result = self._values.get("statement_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def with_event(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.'''
        result = self._values.get("with_event")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRedshiftTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRedshiftTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRedshiftTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRedshiftTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDbUser")
    def reset_db_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbUser", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetSql")
    def reset_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSql", []))

    @jsii.member(jsii_name="resetStatementName")
    def reset_statement_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementName", []))

    @jsii.member(jsii_name="resetWithEvent")
    def reset_with_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithEvent", []))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dbUserInput")
    def db_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbUserInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInput")
    def sql_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlInput"))

    @builtins.property
    @jsii.member(jsii_name="statementNameInput")
    def statement_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="withEventInput")
    def with_event_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withEventInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="dbUser")
    def db_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbUser"))

    @db_user.setter
    def db_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "db_user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbUser", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "secrets_manager_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="sql")
    def sql(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sql"))

    @sql.setter
    def sql(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "sql").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sql", value)

    @builtins.property
    @jsii.member(jsii_name="statementName")
    def statement_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementName"))

    @statement_name.setter
    def statement_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "statement_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementName", value)

    @builtins.property
    @jsii.member(jsii_name="withEvent")
    def with_event(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withEvent"))

    @with_event.setter
    def with_event(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "with_event").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withEvent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetRedshiftTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetRedshiftTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetRedshiftTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRedshiftTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
    },
)
class CloudwatchEventTargetRetryPolicy:
    def __init__(
        self,
        *,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRetryPolicy.__init__)
            check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
            check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
        self._values: typing.Dict[str, typing.Any] = {}
        if maximum_event_age_in_seconds is not None:
            self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts

    @builtins.property
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.'''
        result = self._values.get("maximum_event_age_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.'''
        result = self._values.get("maximum_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRetryPolicyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaximumEventAgeInSeconds")
    def reset_maximum_event_age_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumEventAgeInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRetryAttempts")
    def reset_maximum_retry_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRetryAttempts", []))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSecondsInput")
    def maximum_event_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEventAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttemptsInput")
    def maximum_retry_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRetryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEventAgeInSeconds"))

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRetryPolicyOutputReference, "maximum_event_age_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEventAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRetryAttempts"))

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRetryPolicyOutputReference, "maximum_retry_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetRetryPolicy]:
        return typing.cast(typing.Optional[CloudwatchEventTargetRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRunCommandTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class CloudwatchEventTargetRunCommandTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#key CloudwatchEventTarget#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#values CloudwatchEventTarget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRunCommandTargets.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#key CloudwatchEventTarget#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#values CloudwatchEventTarget#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRunCommandTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRunCommandTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRunCommandTargetsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRunCommandTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventTargetRunCommandTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRunCommandTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventTargetRunCommandTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetRunCommandTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetRunCommandTargetsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetRunCommandTargetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetRunCommandTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetSqsTarget",
    jsii_struct_bases=[],
    name_mapping={"message_group_id": "messageGroupId"},
)
class CloudwatchEventTargetSqsTarget:
    def __init__(
        self,
        *,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetSqsTarget.__init__)
            check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message_group_id is not None:
            self._values["message_group_id"] = message_group_id

    @builtins.property
    def message_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.'''
        result = self._values.get("message_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetSqsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetSqsTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.CloudwatchEventTargetSqsTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudwatchEventTargetSqsTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessageGroupId")
    def reset_message_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="messageGroupIdInput")
    def message_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="messageGroupId")
    def message_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageGroupId"))

    @message_group_id.setter
    def message_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetSqsTargetOutputReference, "message_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetSqsTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetSqsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetSqsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudwatchEventTargetSqsTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCloudwatchEventBus(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventBus",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus aws_cloudwatch_event_bus}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus aws_cloudwatch_event_bus} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#name DataAwsCloudwatchEventBus#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#id DataAwsCloudwatchEventBus#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventBus.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsCloudwatchEventBusConfig(
            name=name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventBus, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventBus, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventBusConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "id": "id",
    },
)
class DataAwsCloudwatchEventBusConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#name DataAwsCloudwatchEventBus#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#id DataAwsCloudwatchEventBus#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventBusConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#name DataAwsCloudwatchEventBus#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_bus#id DataAwsCloudwatchEventBus#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCloudwatchEventBusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCloudwatchEventConnection(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection aws_cloudwatch_event_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection aws_cloudwatch_event_connection} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#name DataAwsCloudwatchEventConnection#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#id DataAwsCloudwatchEventConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsCloudwatchEventConnectionConfig(
            name=name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationType"))

    @builtins.property
    @jsii.member(jsii_name="secretArn")
    def secret_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretArn"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "id": "id",
    },
)
class DataAwsCloudwatchEventConnectionConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#name DataAwsCloudwatchEventConnection#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#id DataAwsCloudwatchEventConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#name DataAwsCloudwatchEventConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_connection#id DataAwsCloudwatchEventConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCloudwatchEventConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCloudwatchEventSource(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventSource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source aws_cloudwatch_event_source}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source aws_cloudwatch_event_source} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#id DataAwsCloudwatchEventSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#name_prefix DataAwsCloudwatchEventSource#name_prefix}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventSource.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsCloudwatchEventSourceConfig(
            id=id,
            name_prefix=name_prefix,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventSource, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsCloudwatchEventSource, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.eventbridge.DataAwsCloudwatchEventSourceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "name_prefix": "namePrefix",
    },
)
class DataAwsCloudwatchEventSourceConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS CloudWatch Event Bridge.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#id DataAwsCloudwatchEventSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#name_prefix DataAwsCloudwatchEventSource#name_prefix}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsCloudwatchEventSourceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#id DataAwsCloudwatchEventSource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/cloudwatch_event_source#name_prefix DataAwsCloudwatchEventSource#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCloudwatchEventSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudwatchEventApiDestination",
    "CloudwatchEventApiDestinationConfig",
    "CloudwatchEventArchive",
    "CloudwatchEventArchiveConfig",
    "CloudwatchEventBus",
    "CloudwatchEventBusConfig",
    "CloudwatchEventBusPolicy",
    "CloudwatchEventBusPolicyConfig",
    "CloudwatchEventConnection",
    "CloudwatchEventConnectionAuthParameters",
    "CloudwatchEventConnectionAuthParametersApiKey",
    "CloudwatchEventConnectionAuthParametersApiKeyOutputReference",
    "CloudwatchEventConnectionAuthParametersBasic",
    "CloudwatchEventConnectionAuthParametersBasicOutputReference",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParameters",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersBody",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyList",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersBodyOutputReference",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeader",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderList",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersHeaderOutputReference",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersOutputReference",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryString",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringList",
    "CloudwatchEventConnectionAuthParametersInvocationHttpParametersQueryStringOutputReference",
    "CloudwatchEventConnectionAuthParametersOauth",
    "CloudwatchEventConnectionAuthParametersOauthClientParameters",
    "CloudwatchEventConnectionAuthParametersOauthClientParametersOutputReference",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParameters",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBody",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyList",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersBodyOutputReference",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeader",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderList",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersHeaderOutputReference",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersOutputReference",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryString",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringList",
    "CloudwatchEventConnectionAuthParametersOauthOauthHttpParametersQueryStringOutputReference",
    "CloudwatchEventConnectionAuthParametersOauthOutputReference",
    "CloudwatchEventConnectionAuthParametersOutputReference",
    "CloudwatchEventConnectionConfig",
    "CloudwatchEventPermission",
    "CloudwatchEventPermissionCondition",
    "CloudwatchEventPermissionConditionOutputReference",
    "CloudwatchEventPermissionConfig",
    "CloudwatchEventRule",
    "CloudwatchEventRuleConfig",
    "CloudwatchEventTarget",
    "CloudwatchEventTargetBatchTarget",
    "CloudwatchEventTargetBatchTargetOutputReference",
    "CloudwatchEventTargetConfig",
    "CloudwatchEventTargetDeadLetterConfig",
    "CloudwatchEventTargetDeadLetterConfigOutputReference",
    "CloudwatchEventTargetEcsTarget",
    "CloudwatchEventTargetEcsTargetNetworkConfiguration",
    "CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference",
    "CloudwatchEventTargetEcsTargetOutputReference",
    "CloudwatchEventTargetEcsTargetPlacementConstraint",
    "CloudwatchEventTargetEcsTargetPlacementConstraintList",
    "CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference",
    "CloudwatchEventTargetHttpTarget",
    "CloudwatchEventTargetHttpTargetOutputReference",
    "CloudwatchEventTargetInputTransformer",
    "CloudwatchEventTargetInputTransformerOutputReference",
    "CloudwatchEventTargetKinesisTarget",
    "CloudwatchEventTargetKinesisTargetOutputReference",
    "CloudwatchEventTargetRedshiftTarget",
    "CloudwatchEventTargetRedshiftTargetOutputReference",
    "CloudwatchEventTargetRetryPolicy",
    "CloudwatchEventTargetRetryPolicyOutputReference",
    "CloudwatchEventTargetRunCommandTargets",
    "CloudwatchEventTargetRunCommandTargetsList",
    "CloudwatchEventTargetRunCommandTargetsOutputReference",
    "CloudwatchEventTargetSqsTarget",
    "CloudwatchEventTargetSqsTargetOutputReference",
    "DataAwsCloudwatchEventBus",
    "DataAwsCloudwatchEventBusConfig",
    "DataAwsCloudwatchEventConnection",
    "DataAwsCloudwatchEventConnectionConfig",
    "DataAwsCloudwatchEventSource",
    "DataAwsCloudwatchEventSourceConfig",
]

publication.publish()
