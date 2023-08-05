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


class AppsyncApiCache(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncApiCache",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache aws_appsync_api_cache}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache aws_appsync_api_cache} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_caching_behavior AppsyncApiCache#api_caching_behavior}.
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_id AppsyncApiCache#api_id}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#ttl AppsyncApiCache#ttl}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#type AppsyncApiCache#type}.
        :param at_rest_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#at_rest_encryption_enabled AppsyncApiCache#at_rest_encryption_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#id AppsyncApiCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param transit_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#transit_encryption_enabled AppsyncApiCache#transit_encryption_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncApiCache.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncApiCacheConfig(
            api_caching_behavior=api_caching_behavior,
            api_id=api_id,
            ttl=ttl,
            type=type,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            id=id,
            transit_encryption_enabled=transit_encryption_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAtRestEncryptionEnabled")
    def reset_at_rest_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAtRestEncryptionEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTransitEncryptionEnabled")
    def reset_transit_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryptionEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiCachingBehaviorInput")
    def api_caching_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiCachingBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabledInput")
    def at_rest_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "atRestEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabledInput")
    def transit_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "transitEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiCachingBehavior")
    def api_caching_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiCachingBehavior"))

    @api_caching_behavior.setter
    def api_caching_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "api_caching_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "at_rest_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "transit_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiCache, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncApiCacheConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_caching_behavior": "apiCachingBehavior",
        "api_id": "apiId",
        "ttl": "ttl",
        "type": "type",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "id": "id",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class AppsyncApiCacheConfig(cdktf.TerraformMetaArguments):
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
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_caching_behavior AppsyncApiCache#api_caching_behavior}.
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_id AppsyncApiCache#api_id}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#ttl AppsyncApiCache#ttl}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#type AppsyncApiCache#type}.
        :param at_rest_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#at_rest_encryption_enabled AppsyncApiCache#at_rest_encryption_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#id AppsyncApiCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param transit_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#transit_encryption_enabled AppsyncApiCache#transit_encryption_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncApiCacheConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_caching_behavior", value=api_caching_behavior, expected_type=type_hints["api_caching_behavior"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_caching_behavior": api_caching_behavior,
            "api_id": api_id,
            "ttl": ttl,
            "type": type,
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
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if id is not None:
            self._values["id"] = id
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

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
    def api_caching_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_caching_behavior AppsyncApiCache#api_caching_behavior}.'''
        result = self._values.get("api_caching_behavior")
        assert result is not None, "Required property 'api_caching_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#api_id AppsyncApiCache#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ttl(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#ttl AppsyncApiCache#ttl}.'''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#type AppsyncApiCache#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#at_rest_encryption_enabled AppsyncApiCache#at_rest_encryption_enabled}.'''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#id AppsyncApiCache#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_cache#transit_encryption_enabled AppsyncApiCache#transit_encryption_enabled}.'''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncApiCacheConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncApiKey(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncApiKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key aws_appsync_api_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key aws_appsync_api_key} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#api_id AppsyncApiKey#api_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#description AppsyncApiKey#description}.
        :param expires: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#expires AppsyncApiKey#expires}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#id AppsyncApiKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncApiKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncApiKeyConfig(
            api_id=api_id,
            description=description,
            expires=expires,
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

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExpires")
    def reset_expires(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpires", []))

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
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresInput")
    def expires_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiKey, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiKey, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expires")
    def expires(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expires"))

    @expires.setter
    def expires(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiKey, "expires").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expires", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncApiKey, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncApiKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "description": "description",
        "expires": "expires",
        "id": "id",
    },
)
class AppsyncApiKeyConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#api_id AppsyncApiKey#api_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#description AppsyncApiKey#description}.
        :param expires: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#expires AppsyncApiKey#expires}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#id AppsyncApiKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncApiKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
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
        if expires is not None:
            self._values["expires"] = expires
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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#api_id AppsyncApiKey#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#description AppsyncApiKey#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#expires AppsyncApiKey#expires}.'''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_api_key#id AppsyncApiKey#id}.

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
        return "AppsyncApiKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasource(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasource.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncDatasourceConfig(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamodb_config=dynamodb_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            id=id,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDynamodbConfig")
    def put_dynamodb_config(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        value = AppsyncDatasourceDynamodbConfig(
            table_name=table_name,
            delta_sync_config=delta_sync_config,
            region=region,
            use_caller_credentials=use_caller_credentials,
            versioned=versioned,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamodbConfig", [value]))

    @jsii.member(jsii_name="putElasticsearchConfig")
    def put_elasticsearch_config(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        value = AppsyncDatasourceElasticsearchConfig(endpoint=endpoint, region=region)

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConfig", [value]))

    @jsii.member(jsii_name="putHttpConfig")
    def put_http_config(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        value = AppsyncDatasourceHttpConfig(
            endpoint=endpoint, authorization_config=authorization_config
        )

        return typing.cast(None, jsii.invoke(self, "putHttpConfig", [value]))

    @jsii.member(jsii_name="putLambdaConfig")
    def put_lambda_config(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        value = AppsyncDatasourceLambdaConfig(function_arn=function_arn)

        return typing.cast(None, jsii.invoke(self, "putLambdaConfig", [value]))

    @jsii.member(jsii_name="putRelationalDatabaseConfig")
    def put_relational_database_config(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfig(
            http_endpoint_config=http_endpoint_config, source_type=source_type
        )

        return typing.cast(None, jsii.invoke(self, "putRelationalDatabaseConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodbConfig")
    def reset_dynamodb_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbConfig", []))

    @jsii.member(jsii_name="resetElasticsearchConfig")
    def reset_elasticsearch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConfig", []))

    @jsii.member(jsii_name="resetHttpConfig")
    def reset_http_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaConfig")
    def reset_lambda_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConfig", []))

    @jsii.member(jsii_name="resetRelationalDatabaseConfig")
    def reset_relational_database_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelationalDatabaseConfig", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

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
    @jsii.member(jsii_name="dynamodbConfig")
    def dynamodb_config(self) -> "AppsyncDatasourceDynamodbConfigOutputReference":
        return typing.cast("AppsyncDatasourceDynamodbConfigOutputReference", jsii.get(self, "dynamodbConfig"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> "AppsyncDatasourceElasticsearchConfigOutputReference":
        return typing.cast("AppsyncDatasourceElasticsearchConfigOutputReference", jsii.get(self, "elasticsearchConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(self) -> "AppsyncDatasourceHttpConfigOutputReference":
        return typing.cast("AppsyncDatasourceHttpConfigOutputReference", jsii.get(self, "httpConfig"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(self) -> "AppsyncDatasourceLambdaConfigOutputReference":
        return typing.cast("AppsyncDatasourceLambdaConfigOutputReference", jsii.get(self, "lambdaConfig"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> "AppsyncDatasourceRelationalDatabaseConfigOutputReference":
        return typing.cast("AppsyncDatasourceRelationalDatabaseConfigOutputReference", jsii.get(self, "relationalDatabaseConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbConfigInput")
    def dynamodb_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], jsii.get(self, "dynamodbConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfigInput")
    def elasticsearch_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], jsii.get(self, "elasticsearchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="httpConfigInput")
    def http_config_input(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], jsii.get(self, "httpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfigInput")
    def lambda_config_input(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], jsii.get(self, "lambdaConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfigInput")
    def relational_database_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], jsii.get(self, "relationalDatabaseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "service_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasource, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamodb_config": "dynamodbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "id": "id",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class AppsyncDatasourceConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dynamodb_config, dict):
            dynamodb_config = AppsyncDatasourceDynamodbConfig(**dynamodb_config)
        if isinstance(elasticsearch_config, dict):
            elasticsearch_config = AppsyncDatasourceElasticsearchConfig(**elasticsearch_config)
        if isinstance(http_config, dict):
            http_config = AppsyncDatasourceHttpConfig(**http_config)
        if isinstance(lambda_config, dict):
            lambda_config = AppsyncDatasourceLambdaConfig(**lambda_config)
        if isinstance(relational_database_config, dict):
            relational_database_config = AppsyncDatasourceRelationalDatabaseConfig(**relational_database_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_config", value=dynamodb_config, expected_type=type_hints["dynamodb_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "type": type,
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
        if dynamodb_config is not None:
            self._values["dynamodb_config"] = dynamodb_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if id is not None:
            self._values["id"] = id
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_config(self) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        '''dynamodb_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        '''
        result = self._values.get("dynamodb_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        '''elasticsearch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], result)

    @builtins.property
    def http_config(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        '''http_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_config(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        '''lambda_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        '''relational_database_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceDynamodbConfig",
    jsii_struct_bases=[],
    name_mapping={
        "table_name": "tableName",
        "delta_sync_config": "deltaSyncConfig",
        "region": "region",
        "use_caller_credentials": "useCallerCredentials",
        "versioned": "versioned",
    },
)
class AppsyncDatasourceDynamodbConfig:
    def __init__(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        if isinstance(delta_sync_config, dict):
            delta_sync_config = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(**delta_sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceDynamodbConfig.__init__)
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument delta_sync_config", value=delta_sync_config, expected_type=type_hints["delta_sync_config"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
            check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_name": table_name,
        }
        if delta_sync_config is not None:
            self._values["delta_sync_config"] = delta_sync_config
        if region is not None:
            self._values["region"] = region
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials
        if versioned is not None:
            self._values["versioned"] = versioned

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delta_sync_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"]:
        '''delta_sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        '''
        result = self._values.get("delta_sync_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_caller_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.'''
        result = self._values.get("use_caller_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def versioned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.'''
        result = self._values.get("versioned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "delta_sync_table_name": "deltaSyncTableName",
        "base_table_ttl": "baseTableTtl",
        "delta_sync_table_ttl": "deltaSyncTableTtl",
    },
)
class AppsyncDatasourceDynamodbConfigDeltaSyncConfig:
    def __init__(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceDynamodbConfigDeltaSyncConfig.__init__)
            check_type(argname="argument delta_sync_table_name", value=delta_sync_table_name, expected_type=type_hints["delta_sync_table_name"])
            check_type(argname="argument base_table_ttl", value=base_table_ttl, expected_type=type_hints["base_table_ttl"])
            check_type(argname="argument delta_sync_table_ttl", value=delta_sync_table_ttl, expected_type=type_hints["delta_sync_table_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "delta_sync_table_name": delta_sync_table_name,
        }
        if base_table_ttl is not None:
            self._values["base_table_ttl"] = base_table_ttl
        if delta_sync_table_ttl is not None:
            self._values["delta_sync_table_ttl"] = delta_sync_table_ttl

    @builtins.property
    def delta_sync_table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.'''
        result = self._values.get("delta_sync_table_name")
        assert result is not None, "Required property 'delta_sync_table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.'''
        result = self._values.get("base_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delta_sync_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.'''
        result = self._values.get("delta_sync_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfigDeltaSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBaseTableTtl")
    def reset_base_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseTableTtl", []))

    @jsii.member(jsii_name="resetDeltaSyncTableTtl")
    def reset_delta_sync_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncTableTtl", []))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtlInput")
    def base_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableNameInput")
    def delta_sync_table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deltaSyncTableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtlInput")
    def delta_sync_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deltaSyncTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtl")
    def base_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baseTableTtl"))

    @base_table_ttl.setter
    def base_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, "base_table_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableName")
    def delta_sync_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deltaSyncTableName"))

    @delta_sync_table_name.setter
    def delta_sync_table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, "delta_sync_table_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableName", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtl")
    def delta_sync_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deltaSyncTableTtl"))

    @delta_sync_table_ttl.setter
    def delta_sync_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, "delta_sync_table_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceDynamodbConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceDynamodbConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceDynamodbConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeltaSyncConfig")
    def put_delta_sync_config(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        value = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(
            delta_sync_table_name=delta_sync_table_name,
            base_table_ttl=base_table_ttl,
            delta_sync_table_ttl=delta_sync_table_ttl,
        )

        return typing.cast(None, jsii.invoke(self, "putDeltaSyncConfig", [value]))

    @jsii.member(jsii_name="resetDeltaSyncConfig")
    def reset_delta_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncConfig", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetUseCallerCredentials")
    def reset_use_caller_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCallerCredentials", []))

    @jsii.member(jsii_name="resetVersioned")
    def reset_versioned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioned", []))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfig")
    def delta_sync_config(
        self,
    ) -> AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference:
        return typing.cast(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, jsii.get(self, "deltaSyncConfig"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfigInput")
    def delta_sync_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "deltaSyncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCallerCredentialsInput")
    def use_caller_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCallerCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionedInput")
    def versioned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "versionedInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigOutputReference, "table_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="useCallerCredentials")
    def use_caller_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCallerCredentials"))

    @use_caller_credentials.setter
    def use_caller_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigOutputReference, "use_caller_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCallerCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="versioned")
    def versioned(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "versioned"))

    @versioned.setter
    def versioned(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigOutputReference, "versioned").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versioned", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceDynamodbConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceDynamodbConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceElasticsearchConfig",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint", "region": "region"},
)
class AppsyncDatasourceElasticsearchConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceElasticsearchConfig.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceElasticsearchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceElasticsearchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceElasticsearchConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceElasticsearchConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceElasticsearchConfigOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceElasticsearchConfigOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceElasticsearchConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceElasticsearchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceElasticsearchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceElasticsearchConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class AppsyncDatasourceHttpConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AppsyncDatasourceHttpConfigAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfig.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"]:
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfigAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "aws_iam_config": "awsIamConfig",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfig:
    def __init__(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        if isinstance(aws_iam_config, dict):
            aws_iam_config = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(**aws_iam_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfigAuthorizationConfig.__init__)
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument aws_iam_config", value=aws_iam_config, expected_type=type_hints["aws_iam_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authorization_type is not None:
            self._values["authorization_type"] = authorization_type
        if aws_iam_config is not None:
            self._values["aws_iam_config"] = aws_iam_config

    @builtins.property
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.'''
        result = self._values.get("authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_iam_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"]:
        '''aws_iam_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        result = self._values.get("aws_iam_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig.__init__)
            check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if signing_region is not None:
            self._values["signing_region"] = signing_region
        if signing_service_name is not None:
            self._values["signing_service_name"] = signing_service_name

    @builtins.property
    def signing_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.'''
        result = self._values.get("signing_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.'''
        result = self._values.get("signing_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSigningRegion")
    def reset_signing_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningRegion", []))

    @jsii.member(jsii_name="resetSigningServiceName")
    def reset_signing_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="signingRegionInput")
    def signing_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="signingServiceNameInput")
    def signing_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="signingRegion")
    def signing_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingRegion"))

    @signing_region.setter
    def signing_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, "signing_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingRegion", value)

    @builtins.property
    @jsii.member(jsii_name="signingServiceName")
    def signing_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingServiceName"))

    @signing_service_name.setter
    def signing_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, "signing_service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsIamConfig")
    def put_aws_iam_config(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(
            signing_region=signing_region, signing_service_name=signing_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putAwsIamConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationType")
    def reset_authorization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationType", []))

    @jsii.member(jsii_name="resetAwsIamConfig")
    def reset_aws_iam_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIamConfig", []))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfig")
    def aws_iam_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, jsii.get(self, "awsIamConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationTypeInput")
    def authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfigInput")
    def aws_iam_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "awsIamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationType"))

    @authorization_type.setter
    def authorization_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference, "authorization_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceHttpConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceHttpConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfig(
            authorization_type=authorization_type, aws_iam_config=aws_iam_config
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationConfig")
    def reset_authorization_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceHttpConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceHttpConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceLambdaConfig",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncDatasourceLambdaConfig:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceLambdaConfig.__init__)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceLambdaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceLambdaConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceLambdaConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceLambdaConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceLambdaConfigOutputReference, "function_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceLambdaConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceLambdaConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceLambdaConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceLambdaConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceRelationalDatabaseConfig",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint_config": "httpEndpointConfig",
        "source_type": "sourceType",
    },
)
class AppsyncDatasourceRelationalDatabaseConfig:
    def __init__(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        if isinstance(http_endpoint_config, dict):
            http_endpoint_config = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(**http_endpoint_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceRelationalDatabaseConfig.__init__)
            check_type(argname="argument http_endpoint_config", value=http_endpoint_config, expected_type=type_hints["http_endpoint_config"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_endpoint_config is not None:
            self._values["http_endpoint_config"] = http_endpoint_config
        if source_type is not None:
            self._values["source_type"] = source_type

    @builtins.property
    def http_endpoint_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"]:
        '''http_endpoint_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        '''
        result = self._values.get("http_endpoint_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.'''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aws_secret_store_arn": "awsSecretStoreArn",
        "db_cluster_identifier": "dbClusterIdentifier",
        "database_name": "databaseName",
        "region": "region",
        "schema": "schema",
    },
)
class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig:
    def __init__(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig.__init__)
            check_type(argname="argument aws_secret_store_arn", value=aws_secret_store_arn, expected_type=type_hints["aws_secret_store_arn"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "aws_secret_store_arn": aws_secret_store_arn,
            "db_cluster_identifier": db_cluster_identifier,
        }
        if database_name is not None:
            self._values["database_name"] = database_name
        if region is not None:
            self._values["region"] = region
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def aws_secret_store_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.'''
        result = self._values.get("aws_secret_store_arn")
        assert result is not None, "Required property 'aws_secret_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.'''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArnInput")
    def aws_secret_store_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSecretStoreArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifierInput")
    def db_cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArn")
    def aws_secret_store_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSecretStoreArn"))

    @aws_secret_store_arn.setter
    def aws_secret_store_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "aws_secret_store_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSecretStoreArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "db_cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceRelationalDatabaseConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDatasourceRelationalDatabaseConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncDatasourceRelationalDatabaseConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpEndpointConfig")
    def put_http_endpoint_config(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(
            aws_secret_store_arn=aws_secret_store_arn,
            db_cluster_identifier=db_cluster_identifier,
            database_name=database_name,
            region=region,
            schema=schema,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpEndpointConfig", [value]))

    @jsii.member(jsii_name="resetHttpEndpointConfig")
    def reset_http_endpoint_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpointConfig", []))

    @jsii.member(jsii_name="resetSourceType")
    def reset_source_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceType", []))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfig")
    def http_endpoint_config(
        self,
    ) -> AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference:
        return typing.cast(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, jsii.get(self, "httpEndpointConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfigInput")
    def http_endpoint_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "httpEndpointConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigOutputReference, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDatasourceRelationalDatabaseConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDomainName(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDomainName",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name aws_appsync_domain_name}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_arn: builtins.str,
        domain_name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name aws_appsync_domain_name} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#certificate_arn AppsyncDomainName#certificate_arn}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#domain_name AppsyncDomainName#domain_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#description AppsyncDomainName#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#id AppsyncDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDomainName.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncDomainNameConfig(
            certificate_arn=certificate_arn,
            domain_name=domain_name,
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
    @jsii.member(jsii_name="appsyncDomainName")
    def appsync_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appsyncDomainName"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainName, "certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainName, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainName, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainName, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


class AppsyncDomainNameApiAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDomainNameApiAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association aws_appsync_domain_name_api_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association aws_appsync_domain_name_api_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#api_id AppsyncDomainNameApiAssociation#api_id}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#domain_name AppsyncDomainNameApiAssociation#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#id AppsyncDomainNameApiAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDomainNameApiAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncDomainNameApiAssociationConfig(
            api_id=api_id,
            domain_name=domain_name,
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
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainNameApiAssociation, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainNameApiAssociation, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncDomainNameApiAssociation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDomainNameApiAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "domain_name": "domainName",
        "id": "id",
    },
)
class AppsyncDomainNameApiAssociationConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#api_id AppsyncDomainNameApiAssociation#api_id}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#domain_name AppsyncDomainNameApiAssociation#domain_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#id AppsyncDomainNameApiAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDomainNameApiAssociationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "domain_name": domain_name,
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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#api_id AppsyncDomainNameApiAssociation#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#domain_name AppsyncDomainNameApiAssociation#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name_api_association#id AppsyncDomainNameApiAssociation#id}.

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
        return "AppsyncDomainNameApiAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncDomainNameConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_arn": "certificateArn",
        "domain_name": "domainName",
        "description": "description",
        "id": "id",
    },
)
class AppsyncDomainNameConfig(cdktf.TerraformMetaArguments):
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
        certificate_arn: builtins.str,
        domain_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#certificate_arn AppsyncDomainName#certificate_arn}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#domain_name AppsyncDomainName#domain_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#description AppsyncDomainName#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#id AppsyncDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncDomainNameConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "domain_name": domain_name,
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
    def certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#certificate_arn AppsyncDomainName#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#domain_name AppsyncDomainName#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#description AppsyncDomainName#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_domain_name#id AppsyncDomainName#id}.

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
        return "AppsyncDomainNameConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncFunction(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_function aws_appsync_function}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        data_source: builtins.str,
        name: builtins.str,
        request_mapping_template: builtins.str,
        response_mapping_template: builtins.str,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        sync_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_function aws_appsync_function} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param request_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.
        :param response_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.
        :param function_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncFunction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncFunctionConfig(
            api_id=api_id,
            data_source=data_source,
            name=name,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            description=description,
            function_version=function_version,
            id=id,
            max_batch_size=max_batch_size,
            sync_config=sync_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSyncConfig")
    def put_sync_config(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        value = AppsyncFunctionSyncConfig(
            conflict_detection=conflict_detection,
            conflict_handler=conflict_handler,
            lambda_conflict_handler_config=lambda_conflict_handler_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSyncConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFunctionVersion")
    def reset_function_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxBatchSize")
    def reset_max_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchSize", []))

    @jsii.member(jsii_name="resetSyncConfig")
    def reset_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncConfig", []))

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
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(self) -> "AppsyncFunctionSyncConfigOutputReference":
        return typing.cast("AppsyncFunctionSyncConfigOutputReference", jsii.get(self, "syncConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceInput")
    def data_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="functionVersionInput")
    def function_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchSizeInput")
    def max_batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateInput")
    def request_mapping_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateInput")
    def response_mapping_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="syncConfigInput")
    def sync_config_input(self) -> typing.Optional["AppsyncFunctionSyncConfig"]:
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfig"], jsii.get(self, "syncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "data_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionVersion"))

    @function_version.setter
    def function_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "function_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "max_batch_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "request_mapping_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunction, "response_mapping_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunctionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "data_source": "dataSource",
        "name": "name",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "description": "description",
        "function_version": "functionVersion",
        "id": "id",
        "max_batch_size": "maxBatchSize",
        "sync_config": "syncConfig",
    },
)
class AppsyncFunctionConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        data_source: builtins.str,
        name: builtins.str,
        request_mapping_template: builtins.str,
        response_mapping_template: builtins.str,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        sync_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param request_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.
        :param response_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.
        :param function_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sync_config, dict):
            sync_config = AppsyncFunctionSyncConfig(**sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncFunctionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument function_version", value=function_version, expected_type=type_hints["function_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "data_source": data_source,
            "name": name,
            "request_mapping_template": request_mapping_template,
            "response_mapping_template": response_mapping_template,
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
        if function_version is not None:
            self._values["function_version"] = function_version
        if id is not None:
            self._values["id"] = id
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if sync_config is not None:
            self._values["sync_config"] = sync_config

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.'''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def request_mapping_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.'''
        result = self._values.get("request_mapping_template")
        assert result is not None, "Required property 'request_mapping_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def response_mapping_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.'''
        result = self._values.get("response_mapping_template")
        assert result is not None, "Required property 'response_mapping_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.'''
        result = self._values.get("function_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.'''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sync_config(self) -> typing.Optional["AppsyncFunctionSyncConfig"]:
        '''sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunctionSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "conflict_detection": "conflictDetection",
        "conflict_handler": "conflictHandler",
        "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
    },
)
class AppsyncFunctionSyncConfig:
    def __init__(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        if isinstance(lambda_conflict_handler_config, dict):
            lambda_conflict_handler_config = AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(**lambda_conflict_handler_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncFunctionSyncConfig.__init__)
            check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
            check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
            check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if conflict_detection is not None:
            self._values["conflict_detection"] = conflict_detection
        if conflict_handler is not None:
            self._values["conflict_handler"] = conflict_handler
        if lambda_conflict_handler_config is not None:
            self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

    @builtins.property
    def conflict_detection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.'''
        result = self._values.get("conflict_detection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conflict_handler(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.'''
        result = self._values.get("conflict_handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_conflict_handler_config(
        self,
    ) -> typing.Optional["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig"]:
        '''lambda_conflict_handler_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        result = self._values.get("lambda_conflict_handler_config")
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunctionSyncConfigLambdaConflictHandlerConfig",
    jsii_struct_bases=[],
    name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
)
class AppsyncFunctionSyncConfigLambdaConflictHandlerConfig:
    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncFunctionSyncConfigLambdaConflictHandlerConfig.__init__)
            check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if lambda_conflict_handler_arn is not None:
            self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

    @builtins.property
    def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.'''
        result = self._values.get("lambda_conflict_handler_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLambdaConflictHandlerArn")
    def reset_lambda_conflict_handler_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerArn", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArnInput")
    def lambda_conflict_handler_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaConflictHandlerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaConflictHandlerArn"))

    @lambda_conflict_handler_arn.setter
    def lambda_conflict_handler_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference, "lambda_conflict_handler_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConflictHandlerArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncFunctionSyncConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncFunctionSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncFunctionSyncConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLambdaConflictHandlerConfig")
    def put_lambda_conflict_handler_config(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.
        '''
        value = AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(
            lambda_conflict_handler_arn=lambda_conflict_handler_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaConflictHandlerConfig", [value]))

    @jsii.member(jsii_name="resetConflictDetection")
    def reset_conflict_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictDetection", []))

    @jsii.member(jsii_name="resetConflictHandler")
    def reset_conflict_handler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictHandler", []))

    @jsii.member(jsii_name="resetLambdaConflictHandlerConfig")
    def reset_lambda_conflict_handler_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(
        self,
    ) -> AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference:
        return typing.cast(AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference, jsii.get(self, "lambdaConflictHandlerConfig"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetectionInput")
    def conflict_detection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictHandlerInput")
    def conflict_handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictHandlerInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfigInput")
    def lambda_conflict_handler_config_input(
        self,
    ) -> typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "lambdaConflictHandlerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetection")
    def conflict_detection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictDetection"))

    @conflict_detection.setter
    def conflict_detection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunctionSyncConfigOutputReference, "conflict_detection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictDetection", value)

    @builtins.property
    @jsii.member(jsii_name="conflictHandler")
    def conflict_handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictHandler"))

    @conflict_handler.setter
    def conflict_handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunctionSyncConfigOutputReference, "conflict_handler").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictHandler", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncFunctionSyncConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncFunctionSyncConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncFunctionSyncConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncGraphqlApi(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApi",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api aws_appsync_graphql_api}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_provider: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProvider", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiLambdaAuthorizerConfig", typing.Dict[str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["AppsyncGraphqlApiLogConfig", typing.Dict[str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiOpenidConnectConfig", typing.Dict[str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiUserPoolConfig", typing.Dict[str, typing.Any]]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api aws_appsync_graphql_api} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.
        :param additional_authentication_provider: additional_authentication_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        :param xray_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApi.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncGraphqlApiConfig(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_provider=additional_authentication_provider,
            id=id,
            lambda_authorizer_config=lambda_authorizer_config,
            log_config=log_config,
            openid_connect_config=openid_connect_config,
            schema=schema,
            tags=tags,
            tags_all=tags_all,
            user_pool_config=user_pool_config,
            xray_enabled=xray_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdditionalAuthenticationProvider")
    def put_additional_authentication_provider(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProvider", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApi.put_additional_authentication_provider)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalAuthenticationProvider", [value]))

    @jsii.member(jsii_name="putLambdaAuthorizerConfig")
    def put_lambda_authorizer_config(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        value = AppsyncGraphqlApiLambdaAuthorizerConfig(
            authorizer_uri=authorizer_uri,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            identity_validation_expression=identity_validation_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaAuthorizerConfig", [value]))

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(
        self,
        *,
        cloudwatch_logs_role_arn: builtins.str,
        field_log_level: builtins.str,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.
        :param field_log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.
        :param exclude_verbose_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.
        '''
        value = AppsyncGraphqlApiLogConfig(
            cloudwatch_logs_role_arn=cloudwatch_logs_role_arn,
            field_log_level=field_log_level,
            exclude_verbose_content=exclude_verbose_content,
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putOpenidConnectConfig")
    def put_openid_connect_config(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        value = AppsyncGraphqlApiOpenidConnectConfig(
            issuer=issuer, auth_ttl=auth_ttl, client_id=client_id, iat_ttl=iat_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putOpenidConnectConfig", [value]))

    @jsii.member(jsii_name="putUserPoolConfig")
    def put_user_pool_config(
        self,
        *,
        default_action: builtins.str,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        value = AppsyncGraphqlApiUserPoolConfig(
            default_action=default_action,
            user_pool_id=user_pool_id,
            app_id_client_regex=app_id_client_regex,
            aws_region=aws_region,
        )

        return typing.cast(None, jsii.invoke(self, "putUserPoolConfig", [value]))

    @jsii.member(jsii_name="resetAdditionalAuthenticationProvider")
    def reset_additional_authentication_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalAuthenticationProvider", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaAuthorizerConfig")
    def reset_lambda_authorizer_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaAuthorizerConfig", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetOpenidConnectConfig")
    def reset_openid_connect_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidConnectConfig", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUserPoolConfig")
    def reset_user_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserPoolConfig", []))

    @jsii.member(jsii_name="resetXrayEnabled")
    def reset_xray_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXrayEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProvider")
    def additional_authentication_provider(
        self,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderList":
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderList", jsii.get(self, "additionalAuthenticationProvider"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> "AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference", jsii.get(self, "lambdaAuthorizerConfig"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "AppsyncGraphqlApiLogConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> "AppsyncGraphqlApiOpenidConnectConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiOpenidConnectConfigOutputReference", jsii.get(self, "openidConnectConfig"))

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "uris"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(self) -> "AppsyncGraphqlApiUserPoolConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiUserPoolConfigOutputReference", jsii.get(self, "userPoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProviderInput")
    def additional_authentication_provider_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppsyncGraphqlApiAdditionalAuthenticationProvider"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppsyncGraphqlApiAdditionalAuthenticationProvider"]]], jsii.get(self, "additionalAuthenticationProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfigInput")
    def lambda_authorizer_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"], jsii.get(self, "lambdaAuthorizerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(self) -> typing.Optional["AppsyncGraphqlApiLogConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfigInput")
    def openid_connect_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"], jsii.get(self, "openidConnectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

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
    @jsii.member(jsii_name="userPoolConfigInput")
    def user_pool_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiUserPoolConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiUserPoolConfig"], jsii.get(self, "userPoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="xrayEnabledInput")
    def xray_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "xrayEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "authentication_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "xrayEnabled"))

    @xray_enabled.setter
    def xray_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApi, "xray_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xrayEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProvider",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "openid_connect_config": "openidConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProvider:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig", typing.Dict[str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig", typing.Dict[str, typing.Any]]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(openid_connect_config, dict):
            openid_connect_config = AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(**openid_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProvider.__init__)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument openid_connect_config", value=openid_connect_config, expected_type=type_hints["openid_connect_config"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_type": authentication_type,
        }
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if openid_connect_config is not None:
            self._values["openid_connect_config"] = openid_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig"]:
        '''lambda_authorizer_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig"], result)

    @builtins.property
    def openid_connect_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig"]:
        '''openid_connect_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        '''
        result = self._values.get("openid_connect_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig"], result)

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"]:
        '''user_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_uri": "authorizerUri",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "identity_validation_expression": "identityValidationExpression",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig.__init__)
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorizer_uri": authorizer_uri,
        }
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression

    @builtins.property
    def authorizer_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.'''
        result = self._values.get("authorizer_uri")
        assert result is not None, "Required property 'authorizer_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.'''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.'''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorizerResultTtlInSeconds")
    def reset_authorizer_result_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerResultTtlInSeconds", []))

    @jsii.member(jsii_name="resetIdentityValidationExpression")
    def reset_identity_validation_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityValidationExpression", []))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSecondsInput")
    def authorizer_result_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerUriInput")
    def authorizer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpressionInput")
    def identity_validation_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityValidationExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, "authorizer_result_ttl_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, "authorizer_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityValidationExpression"))

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, "identity_validation_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncGraphqlApiAdditionalAuthenticationProviderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderList",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "issuer": "issuer",
        "auth_ttl": "authTtl",
        "client_id": "clientId",
        "iat_ttl": "iatTtl",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig:
    def __init__(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig.__init__)
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "issuer": issuer,
        }
        if auth_ttl is not None:
            self._values["auth_ttl"] = auth_ttl
        if client_id is not None:
            self._values["client_id"] = client_id
        if iat_ttl is not None:
            self._values["iat_ttl"] = iat_ttl

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.'''
        result = self._values.get("auth_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iat_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.'''
        result = self._values.get("iat_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthTtl")
    def reset_auth_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthTtl", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetIatTtl")
    def reset_iat_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIatTtl", []))

    @builtins.property
    @jsii.member(jsii_name="authTtlInput")
    def auth_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iatTtlInput")
    def iat_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iatTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="authTtl")
    def auth_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authTtl"))

    @auth_ttl.setter
    def auth_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, "auth_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authTtl", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="iatTtl")
    def iat_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iatTtl"))

    @iat_ttl.setter
    def iat_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, "iat_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iatTtl", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLambdaAuthorizerConfig")
    def put_lambda_authorizer_config(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(
            authorizer_uri=authorizer_uri,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            identity_validation_expression=identity_validation_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaAuthorizerConfig", [value]))

    @jsii.member(jsii_name="putOpenidConnectConfig")
    def put_openid_connect_config(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig(
            issuer=issuer, auth_ttl=auth_ttl, client_id=client_id, iat_ttl=iat_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putOpenidConnectConfig", [value]))

    @jsii.member(jsii_name="putUserPoolConfig")
    def put_user_pool_config(
        self,
        *,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        value = AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(
            user_pool_id=user_pool_id,
            app_id_client_regex=app_id_client_regex,
            aws_region=aws_region,
        )

        return typing.cast(None, jsii.invoke(self, "putUserPoolConfig", [value]))

    @jsii.member(jsii_name="resetLambdaAuthorizerConfig")
    def reset_lambda_authorizer_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaAuthorizerConfig", []))

    @jsii.member(jsii_name="resetOpenidConnectConfig")
    def reset_openid_connect_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidConnectConfig", []))

    @jsii.member(jsii_name="resetUserPoolConfig")
    def reset_user_pool_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserPoolConfig", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference:
        return typing.cast(AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference, jsii.get(self, "lambdaAuthorizerConfig"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference:
        return typing.cast(AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference, jsii.get(self, "openidConnectConfig"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference":
        return typing.cast("AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference", jsii.get(self, "userPoolConfig"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAuthorizerConfigInput")
    def lambda_authorizer_config_input(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig], jsii.get(self, "lambdaAuthorizerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectConfigInput")
    def openid_connect_config_input(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig], jsii.get(self, "openidConnectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolConfigInput")
    def user_pool_config_input(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"]:
        return typing.cast(typing.Optional["AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig"], jsii.get(self, "userPoolConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference, "authentication_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool_id": "userPoolId",
        "app_id_client_regex": "appIdClientRegex",
        "aws_region": "awsRegion",
    },
)
class AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig:
    def __init__(
        self,
        *,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig.__init__)
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_pool_id": user_pool_id,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if aws_region is not None:
            self._values["aws_region"] = aws_region

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.'''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppIdClientRegex")
    def reset_app_id_client_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppIdClientRegex", []))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegexInput")
    def app_id_client_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdClientRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegex")
    def app_id_client_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appIdClientRegex"))

    @app_id_client_regex.setter
    def app_id_client_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference, "app_id_client_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appIdClientRegex", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference, "aws_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference, "user_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_provider": "additionalAuthenticationProvider",
        "id": "id",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "log_config": "logConfig",
        "openid_connect_config": "openidConnectConfig",
        "schema": "schema",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_pool_config": "userPoolConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class AppsyncGraphqlApiConfig(cdktf.TerraformMetaArguments):
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
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_provider: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppsyncGraphqlApiAdditionalAuthenticationProvider, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["AppsyncGraphqlApiLambdaAuthorizerConfig", typing.Dict[str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["AppsyncGraphqlApiLogConfig", typing.Dict[str, typing.Any]]] = None,
        openid_connect_config: typing.Optional[typing.Union["AppsyncGraphqlApiOpenidConnectConfig", typing.Dict[str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_pool_config: typing.Optional[typing.Union["AppsyncGraphqlApiUserPoolConfig", typing.Dict[str, typing.Any]]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.
        :param additional_authentication_provider: additional_authentication_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_authorizer_config: lambda_authorizer_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        :param openid_connect_config: openid_connect_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.
        :param user_pool_config: user_pool_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        :param xray_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = AppsyncGraphqlApiLambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(log_config, dict):
            log_config = AppsyncGraphqlApiLogConfig(**log_config)
        if isinstance(openid_connect_config, dict):
            openid_connect_config = AppsyncGraphqlApiOpenidConnectConfig(**openid_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = AppsyncGraphqlApiUserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_authentication_provider", value=additional_authentication_provider, expected_type=type_hints["additional_authentication_provider"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument openid_connect_config", value=openid_connect_config, expected_type=type_hints["openid_connect_config"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_type": authentication_type,
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
        if additional_authentication_provider is not None:
            self._values["additional_authentication_provider"] = additional_authentication_provider
        if id is not None:
            self._values["id"] = id
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if openid_connect_config is not None:
            self._values["openid_connect_config"] = openid_connect_config
        if schema is not None:
            self._values["schema"] = schema
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

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
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authentication_type AppsyncGraphqlApi#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#name AppsyncGraphqlApi#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_authentication_provider(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]]:
        '''additional_authentication_provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#additional_authentication_provider AppsyncGraphqlApi#additional_authentication_provider}
        '''
        result = self._values.get("additional_authentication_provider")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppsyncGraphqlApiAdditionalAuthenticationProvider]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#id AppsyncGraphqlApi#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_authorizer_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"]:
        '''lambda_authorizer_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#lambda_authorizer_config AppsyncGraphqlApi#lambda_authorizer_config}
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiLambdaAuthorizerConfig"], result)

    @builtins.property
    def log_config(self) -> typing.Optional["AppsyncGraphqlApiLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#log_config AppsyncGraphqlApi#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiLogConfig"], result)

    @builtins.property
    def openid_connect_config(
        self,
    ) -> typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"]:
        '''openid_connect_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#openid_connect_config AppsyncGraphqlApi#openid_connect_config}
        '''
        result = self._values.get("openid_connect_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiOpenidConnectConfig"], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#schema AppsyncGraphqlApi#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags AppsyncGraphqlApi#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#tags_all AppsyncGraphqlApi#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_pool_config(self) -> typing.Optional["AppsyncGraphqlApiUserPoolConfig"]:
        '''user_pool_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_config AppsyncGraphqlApi#user_pool_config}
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["AppsyncGraphqlApiUserPoolConfig"], result)

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#xray_enabled AppsyncGraphqlApi#xray_enabled}.'''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiLambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_uri": "authorizerUri",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "identity_validation_expression": "identityValidationExpression",
    },
)
class AppsyncGraphqlApiLambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        authorizer_uri: builtins.str,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.
        :param identity_validation_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiLambdaAuthorizerConfig.__init__)
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorizer_uri": authorizer_uri,
        }
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression

    @builtins.property
    def authorizer_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_uri AppsyncGraphqlApi#authorizer_uri}.'''
        result = self._values.get("authorizer_uri")
        assert result is not None, "Required property 'authorizer_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#authorizer_result_ttl_in_seconds AppsyncGraphqlApi#authorizer_result_ttl_in_seconds}.'''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#identity_validation_expression AppsyncGraphqlApi#identity_validation_expression}.'''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiLambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorizerResultTtlInSeconds")
    def reset_authorizer_result_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerResultTtlInSeconds", []))

    @jsii.member(jsii_name="resetIdentityValidationExpression")
    def reset_identity_validation_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityValidationExpression", []))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSecondsInput")
    def authorizer_result_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerUriInput")
    def authorizer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpressionInput")
    def identity_validation_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityValidationExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference, "authorizer_result_ttl_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference, "authorizer_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityValidationExpression"))

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference, "identity_validation_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiLambdaAuthorizerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiLogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs_role_arn": "cloudwatchLogsRoleArn",
        "field_log_level": "fieldLogLevel",
        "exclude_verbose_content": "excludeVerboseContent",
    },
)
class AppsyncGraphqlApiLogConfig:
    def __init__(
        self,
        *,
        cloudwatch_logs_role_arn: builtins.str,
        field_log_level: builtins.str,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.
        :param field_log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.
        :param exclude_verbose_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiLogConfig.__init__)
            check_type(argname="argument cloudwatch_logs_role_arn", value=cloudwatch_logs_role_arn, expected_type=type_hints["cloudwatch_logs_role_arn"])
            check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudwatch_logs_role_arn": cloudwatch_logs_role_arn,
            "field_log_level": field_log_level,
        }
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content

    @builtins.property
    def cloudwatch_logs_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#cloudwatch_logs_role_arn AppsyncGraphqlApi#cloudwatch_logs_role_arn}.'''
        result = self._values.get("cloudwatch_logs_role_arn")
        assert result is not None, "Required property 'cloudwatch_logs_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_log_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#field_log_level AppsyncGraphqlApi#field_log_level}.'''
        result = self._values.get("field_log_level")
        assert result is not None, "Required property 'field_log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#exclude_verbose_content AppsyncGraphqlApi#exclude_verbose_content}.'''
        result = self._values.get("exclude_verbose_content")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeVerboseContent")
    def reset_exclude_verbose_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeVerboseContent", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsRoleArnInput")
    def cloudwatch_logs_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeVerboseContentInput")
    def exclude_verbose_content_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeVerboseContentInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldLogLevelInput")
    def field_log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldLogLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogsRoleArn"))

    @cloudwatch_logs_role_arn.setter
    def cloudwatch_logs_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLogConfigOutputReference, "cloudwatch_logs_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="excludeVerboseContent")
    def exclude_verbose_content(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeVerboseContent"))

    @exclude_verbose_content.setter
    def exclude_verbose_content(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLogConfigOutputReference, "exclude_verbose_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeVerboseContent", value)

    @builtins.property
    @jsii.member(jsii_name="fieldLogLevel")
    def field_log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldLogLevel"))

    @field_log_level.setter
    def field_log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLogConfigOutputReference, "field_log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldLogLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiLogConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiOpenidConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "issuer": "issuer",
        "auth_ttl": "authTtl",
        "client_id": "clientId",
        "iat_ttl": "iatTtl",
    },
)
class AppsyncGraphqlApiOpenidConnectConfig:
    def __init__(
        self,
        *,
        issuer: builtins.str,
        auth_ttl: typing.Optional[jsii.Number] = None,
        client_id: typing.Optional[builtins.str] = None,
        iat_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.
        :param auth_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.
        :param iat_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiOpenidConnectConfig.__init__)
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument auth_ttl", value=auth_ttl, expected_type=type_hints["auth_ttl"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument iat_ttl", value=iat_ttl, expected_type=type_hints["iat_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "issuer": issuer,
        }
        if auth_ttl is not None:
            self._values["auth_ttl"] = auth_ttl
        if client_id is not None:
            self._values["client_id"] = client_id
        if iat_ttl is not None:
            self._values["iat_ttl"] = iat_ttl

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#issuer AppsyncGraphqlApi#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#auth_ttl AppsyncGraphqlApi#auth_ttl}.'''
        result = self._values.get("auth_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#client_id AppsyncGraphqlApi#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iat_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#iat_ttl AppsyncGraphqlApi#iat_ttl}.'''
        result = self._values.get("iat_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiOpenidConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiOpenidConnectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiOpenidConnectConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiOpenidConnectConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthTtl")
    def reset_auth_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthTtl", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetIatTtl")
    def reset_iat_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIatTtl", []))

    @builtins.property
    @jsii.member(jsii_name="authTtlInput")
    def auth_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iatTtlInput")
    def iat_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iatTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="authTtl")
    def auth_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authTtl"))

    @auth_ttl.setter
    def auth_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiOpenidConnectConfigOutputReference, "auth_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authTtl", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiOpenidConnectConfigOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="iatTtl")
    def iat_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iatTtl"))

    @iat_ttl.setter
    def iat_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiOpenidConnectConfigOutputReference, "iat_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iatTtl", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiOpenidConnectConfigOutputReference, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiOpenidConnectConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiOpenidConnectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiOpenidConnectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiOpenidConnectConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiUserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "user_pool_id": "userPoolId",
        "app_id_client_regex": "appIdClientRegex",
        "aws_region": "awsRegion",
    },
)
class AppsyncGraphqlApiUserPoolConfig:
    def __init__(
        self,
        *,
        default_action: builtins.str,
        user_pool_id: builtins.str,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.
        :param app_id_client_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncGraphqlApiUserPoolConfig.__init__)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
            "user_pool_id": user_pool_id,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if aws_region is not None:
            self._values["aws_region"] = aws_region

    @builtins.property
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#default_action AppsyncGraphqlApi#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#user_pool_id AppsyncGraphqlApi#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#app_id_client_regex AppsyncGraphqlApi#app_id_client_regex}.'''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_graphql_api#aws_region AppsyncGraphqlApi#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncGraphqlApiUserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncGraphqlApiUserPoolConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncGraphqlApiUserPoolConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncGraphqlApiUserPoolConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppIdClientRegex")
    def reset_app_id_client_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppIdClientRegex", []))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegexInput")
    def app_id_client_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdClientRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appIdClientRegex")
    def app_id_client_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appIdClientRegex"))

    @app_id_client_regex.setter
    def app_id_client_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiUserPoolConfigOutputReference, "app_id_client_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appIdClientRegex", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiUserPoolConfigOutputReference, "aws_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiUserPoolConfigOutputReference, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiUserPoolConfigOutputReference, "user_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncGraphqlApiUserPoolConfig]:
        return typing.cast(typing.Optional[AppsyncGraphqlApiUserPoolConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncGraphqlApiUserPoolConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncGraphqlApiUserPoolConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncResolver(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolver",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver aws_appsync_resolver}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        field: builtins.str,
        type: builtins.str,
        caching_config: typing.Optional[typing.Union["AppsyncResolverCachingConfig", typing.Dict[str, typing.Any]]] = None,
        data_source: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union["AppsyncResolverPipelineConfig", typing.Dict[str, typing.Any]]] = None,
        request_template: typing.Optional[builtins.str] = None,
        response_template: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union["AppsyncResolverSyncConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver aws_appsync_resolver} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.
        :param caching_config: caching_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.
        :param pipeline_config: pipeline_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        :param request_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.
        :param response_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolver.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncResolverConfig(
            api_id=api_id,
            field=field,
            type=type,
            caching_config=caching_config,
            data_source=data_source,
            id=id,
            kind=kind,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_template=request_template,
            response_template=response_template,
            sync_config=sync_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCachingConfig")
    def put_caching_config(
        self,
        *,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param caching_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.
        '''
        value = AppsyncResolverCachingConfig(caching_keys=caching_keys, ttl=ttl)

        return typing.cast(None, jsii.invoke(self, "putCachingConfig", [value]))

    @jsii.member(jsii_name="putPipelineConfig")
    def put_pipeline_config(
        self,
        *,
        functions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param functions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.
        '''
        value = AppsyncResolverPipelineConfig(functions=functions)

        return typing.cast(None, jsii.invoke(self, "putPipelineConfig", [value]))

    @jsii.member(jsii_name="putSyncConfig")
    def put_sync_config(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncResolverSyncConfigLambdaConflictHandlerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        value = AppsyncResolverSyncConfig(
            conflict_detection=conflict_detection,
            conflict_handler=conflict_handler,
            lambda_conflict_handler_config=lambda_conflict_handler_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSyncConfig", [value]))

    @jsii.member(jsii_name="resetCachingConfig")
    def reset_caching_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachingConfig", []))

    @jsii.member(jsii_name="resetDataSource")
    def reset_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSource", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetMaxBatchSize")
    def reset_max_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchSize", []))

    @jsii.member(jsii_name="resetPipelineConfig")
    def reset_pipeline_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineConfig", []))

    @jsii.member(jsii_name="resetRequestTemplate")
    def reset_request_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTemplate", []))

    @jsii.member(jsii_name="resetResponseTemplate")
    def reset_response_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseTemplate", []))

    @jsii.member(jsii_name="resetSyncConfig")
    def reset_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncConfig", []))

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
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(self) -> "AppsyncResolverCachingConfigOutputReference":
        return typing.cast("AppsyncResolverCachingConfigOutputReference", jsii.get(self, "cachingConfig"))

    @builtins.property
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(self) -> "AppsyncResolverPipelineConfigOutputReference":
        return typing.cast("AppsyncResolverPipelineConfigOutputReference", jsii.get(self, "pipelineConfig"))

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(self) -> "AppsyncResolverSyncConfigOutputReference":
        return typing.cast("AppsyncResolverSyncConfigOutputReference", jsii.get(self, "syncConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingConfigInput")
    def caching_config_input(self) -> typing.Optional["AppsyncResolverCachingConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverCachingConfig"], jsii.get(self, "cachingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceInput")
    def data_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchSizeInput")
    def max_batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineConfigInput")
    def pipeline_config_input(self) -> typing.Optional["AppsyncResolverPipelineConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverPipelineConfig"], jsii.get(self, "pipelineConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTemplateInput")
    def request_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="responseTemplateInput")
    def response_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="syncConfigInput")
    def sync_config_input(self) -> typing.Optional["AppsyncResolverSyncConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverSyncConfig"], jsii.get(self, "syncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "api_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "data_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "max_batch_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplate")
    def request_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestTemplate"))

    @request_template.setter
    def request_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "request_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseTemplate")
    def response_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseTemplate"))

    @response_template.setter
    def response_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "response_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolver, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverCachingConfig",
    jsii_struct_bases=[],
    name_mapping={"caching_keys": "cachingKeys", "ttl": "ttl"},
)
class AppsyncResolverCachingConfig:
    def __init__(
        self,
        *,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param caching_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolverCachingConfig.__init__)
            check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if caching_keys is not None:
            self._values["caching_keys"] = caching_keys
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.'''
        result = self._values.get("caching_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverCachingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverCachingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverCachingConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncResolverCachingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCachingKeys")
    def reset_caching_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachingKeys", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="cachingKeysInput")
    def caching_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cachingKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingKeys")
    def caching_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cachingKeys"))

    @caching_keys.setter
    def caching_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverCachingConfigOutputReference, "caching_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingKeys", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverCachingConfigOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverCachingConfig]:
        return typing.cast(typing.Optional[AppsyncResolverCachingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverCachingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverCachingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "field": "field",
        "type": "type",
        "caching_config": "cachingConfig",
        "data_source": "dataSource",
        "id": "id",
        "kind": "kind",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_template": "requestTemplate",
        "response_template": "responseTemplate",
        "sync_config": "syncConfig",
    },
)
class AppsyncResolverConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        field: builtins.str,
        type: builtins.str,
        caching_config: typing.Optional[typing.Union[AppsyncResolverCachingConfig, typing.Dict[str, typing.Any]]] = None,
        data_source: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union["AppsyncResolverPipelineConfig", typing.Dict[str, typing.Any]]] = None,
        request_template: typing.Optional[builtins.str] = None,
        response_template: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union["AppsyncResolverSyncConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS AppSync.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.
        :param caching_config: caching_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.
        :param pipeline_config: pipeline_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        :param request_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.
        :param response_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(caching_config, dict):
            caching_config = AppsyncResolverCachingConfig(**caching_config)
        if isinstance(pipeline_config, dict):
            pipeline_config = AppsyncResolverPipelineConfig(**pipeline_config)
        if isinstance(sync_config, dict):
            sync_config = AppsyncResolverSyncConfig(**sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolverConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_template", value=request_template, expected_type=type_hints["request_template"])
            check_type(argname="argument response_template", value=response_template, expected_type=type_hints["response_template"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "field": field,
            "type": type,
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
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if data_source is not None:
            self._values["data_source"] = data_source
        if id is not None:
            self._values["id"] = id
        if kind is not None:
            self._values["kind"] = kind
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_template is not None:
            self._values["request_template"] = request_template
        if response_template is not None:
            self._values["response_template"] = response_template
        if sync_config is not None:
            self._values["sync_config"] = sync_config

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.'''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[AppsyncResolverCachingConfig]:
        '''caching_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[AppsyncResolverCachingConfig], result)

    @builtins.property
    def data_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.'''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.'''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.'''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional["AppsyncResolverPipelineConfig"]:
        '''pipeline_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional["AppsyncResolverPipelineConfig"], result)

    @builtins.property
    def request_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.'''
        result = self._values.get("request_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.'''
        result = self._values.get("response_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_config(self) -> typing.Optional["AppsyncResolverSyncConfig"]:
        '''sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional["AppsyncResolverSyncConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverPipelineConfig",
    jsii_struct_bases=[],
    name_mapping={"functions": "functions"},
)
class AppsyncResolverPipelineConfig:
    def __init__(
        self,
        *,
        functions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param functions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolverPipelineConfig.__init__)
            check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if functions is not None:
            self._values["functions"] = functions

    @builtins.property
    def functions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.'''
        result = self._values.get("functions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverPipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverPipelineConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverPipelineConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncResolverPipelineConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFunctions")
    def reset_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctions", []))

    @builtins.property
    @jsii.member(jsii_name="functionsInput")
    def functions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "functionsInput"))

    @builtins.property
    @jsii.member(jsii_name="functions")
    def functions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "functions"))

    @functions.setter
    def functions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverPipelineConfigOutputReference, "functions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverPipelineConfig]:
        return typing.cast(typing.Optional[AppsyncResolverPipelineConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverPipelineConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverPipelineConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "conflict_detection": "conflictDetection",
        "conflict_handler": "conflictHandler",
        "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
    },
)
class AppsyncResolverSyncConfig:
    def __init__(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncResolverSyncConfigLambdaConflictHandlerConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        if isinstance(lambda_conflict_handler_config, dict):
            lambda_conflict_handler_config = AppsyncResolverSyncConfigLambdaConflictHandlerConfig(**lambda_conflict_handler_config)
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolverSyncConfig.__init__)
            check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
            check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
            check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if conflict_detection is not None:
            self._values["conflict_detection"] = conflict_detection
        if conflict_handler is not None:
            self._values["conflict_handler"] = conflict_handler
        if lambda_conflict_handler_config is not None:
            self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

    @builtins.property
    def conflict_detection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.'''
        result = self._values.get("conflict_detection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conflict_handler(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.'''
        result = self._values.get("conflict_handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_conflict_handler_config(
        self,
    ) -> typing.Optional["AppsyncResolverSyncConfigLambdaConflictHandlerConfig"]:
        '''lambda_conflict_handler_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        result = self._values.get("lambda_conflict_handler_config")
        return typing.cast(typing.Optional["AppsyncResolverSyncConfigLambdaConflictHandlerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverSyncConfigLambdaConflictHandlerConfig",
    jsii_struct_bases=[],
    name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
)
class AppsyncResolverSyncConfigLambdaConflictHandlerConfig:
    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppsyncResolverSyncConfigLambdaConflictHandlerConfig.__init__)
            check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if lambda_conflict_handler_arn is not None:
            self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

    @builtins.property
    def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.'''
        result = self._values.get("lambda_conflict_handler_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverSyncConfigLambdaConflictHandlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLambdaConflictHandlerArn")
    def reset_lambda_conflict_handler_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerArn", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArnInput")
    def lambda_conflict_handler_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaConflictHandlerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaConflictHandlerArn"))

    @lambda_conflict_handler_arn.setter
    def lambda_conflict_handler_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference, "lambda_conflict_handler_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConflictHandlerArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncResolverSyncConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsync.AppsyncResolverSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(AppsyncResolverSyncConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLambdaConflictHandlerConfig")
    def put_lambda_conflict_handler_config(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.
        '''
        value = AppsyncResolverSyncConfigLambdaConflictHandlerConfig(
            lambda_conflict_handler_arn=lambda_conflict_handler_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaConflictHandlerConfig", [value]))

    @jsii.member(jsii_name="resetConflictDetection")
    def reset_conflict_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictDetection", []))

    @jsii.member(jsii_name="resetConflictHandler")
    def reset_conflict_handler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictHandler", []))

    @jsii.member(jsii_name="resetLambdaConflictHandlerConfig")
    def reset_lambda_conflict_handler_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(
        self,
    ) -> AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference:
        return typing.cast(AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference, jsii.get(self, "lambdaConflictHandlerConfig"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetectionInput")
    def conflict_detection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictHandlerInput")
    def conflict_handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictHandlerInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfigInput")
    def lambda_conflict_handler_config_input(
        self,
    ) -> typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "lambdaConflictHandlerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetection")
    def conflict_detection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictDetection"))

    @conflict_detection.setter
    def conflict_detection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverSyncConfigOutputReference, "conflict_detection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictDetection", value)

    @builtins.property
    @jsii.member(jsii_name="conflictHandler")
    def conflict_handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictHandler"))

    @conflict_handler.setter
    def conflict_handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverSyncConfigOutputReference, "conflict_handler").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictHandler", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverSyncConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncResolverSyncConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppsyncResolverSyncConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncApiCache",
    "AppsyncApiCacheConfig",
    "AppsyncApiKey",
    "AppsyncApiKeyConfig",
    "AppsyncDatasource",
    "AppsyncDatasourceConfig",
    "AppsyncDatasourceDynamodbConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
    "AppsyncDatasourceDynamodbConfigOutputReference",
    "AppsyncDatasourceElasticsearchConfig",
    "AppsyncDatasourceElasticsearchConfigOutputReference",
    "AppsyncDatasourceHttpConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
    "AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
    "AppsyncDatasourceHttpConfigOutputReference",
    "AppsyncDatasourceLambdaConfig",
    "AppsyncDatasourceLambdaConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfigOutputReference",
    "AppsyncDomainName",
    "AppsyncDomainNameApiAssociation",
    "AppsyncDomainNameApiAssociationConfig",
    "AppsyncDomainNameConfig",
    "AppsyncFunction",
    "AppsyncFunctionConfig",
    "AppsyncFunctionSyncConfig",
    "AppsyncFunctionSyncConfigLambdaConflictHandlerConfig",
    "AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference",
    "AppsyncFunctionSyncConfigOutputReference",
    "AppsyncGraphqlApi",
    "AppsyncGraphqlApiAdditionalAuthenticationProvider",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderLambdaAuthorizerConfigOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderList",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOpenidConnectConfigOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderOutputReference",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfig",
    "AppsyncGraphqlApiAdditionalAuthenticationProviderUserPoolConfigOutputReference",
    "AppsyncGraphqlApiConfig",
    "AppsyncGraphqlApiLambdaAuthorizerConfig",
    "AppsyncGraphqlApiLambdaAuthorizerConfigOutputReference",
    "AppsyncGraphqlApiLogConfig",
    "AppsyncGraphqlApiLogConfigOutputReference",
    "AppsyncGraphqlApiOpenidConnectConfig",
    "AppsyncGraphqlApiOpenidConnectConfigOutputReference",
    "AppsyncGraphqlApiUserPoolConfig",
    "AppsyncGraphqlApiUserPoolConfigOutputReference",
    "AppsyncResolver",
    "AppsyncResolverCachingConfig",
    "AppsyncResolverCachingConfigOutputReference",
    "AppsyncResolverConfig",
    "AppsyncResolverPipelineConfig",
    "AppsyncResolverPipelineConfigOutputReference",
    "AppsyncResolverSyncConfig",
    "AppsyncResolverSyncConfigLambdaConflictHandlerConfig",
    "AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference",
    "AppsyncResolverSyncConfigOutputReference",
]

publication.publish()
