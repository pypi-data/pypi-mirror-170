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


class DataAwsLexBot(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexBot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/lex_bot aws_lex_bot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/lex_bot aws_lex_bot} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#name DataAwsLexBot#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#id DataAwsLexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#version DataAwsLexBot#version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexBot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsLexBotConfig(
            name=name,
            id=id,
            version=version,
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

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="childDirected")
    def child_directed(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "childDirected"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="detectSentiment")
    def detect_sentiment(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "detectSentiment"))

    @builtins.property
    @jsii.member(jsii_name="enableModelImprovements")
    def enable_model_improvements(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableModelImprovements"))

    @builtins.property
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureReason"))

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleSessionTtlInSeconds"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locale"))

    @builtins.property
    @jsii.member(jsii_name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nluIntentConfidenceThreshold"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="voiceId")
    def voice_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "voiceId"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBot, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBot, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


class DataAwsLexBotAlias(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexBotAlias",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias aws_lex_bot_alias}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bot_name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias aws_lex_bot_alias} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#bot_name DataAwsLexBotAlias#bot_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#name DataAwsLexBotAlias#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#id DataAwsLexBotAlias#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexBotAlias.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsLexBotAliasConfig(
            bot_name=bot_name,
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
    @jsii.member(jsii_name="botVersion")
    def bot_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "botVersion"))

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="botNameInput")
    def bot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "botNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="botName")
    def bot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "botName"))

    @bot_name.setter
    def bot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBotAlias, "bot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBotAlias, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexBotAlias, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexBotAliasConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bot_name": "botName",
        "name": "name",
        "id": "id",
    },
)
class DataAwsLexBotAliasConfig(cdktf.TerraformMetaArguments):
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
        bot_name: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#bot_name DataAwsLexBotAlias#bot_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#name DataAwsLexBotAlias#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#id DataAwsLexBotAlias#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexBotAliasConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bot_name", value=bot_name, expected_type=type_hints["bot_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "bot_name": bot_name,
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
    def bot_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#bot_name DataAwsLexBotAlias#bot_name}.'''
        result = self._values.get("bot_name")
        assert result is not None, "Required property 'bot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#name DataAwsLexBotAlias#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot_alias#id DataAwsLexBotAlias#id}.

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
        return "DataAwsLexBotAliasConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexBotConfig",
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
        "version": "version",
    },
)
class DataAwsLexBotConfig(cdktf.TerraformMetaArguments):
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
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#name DataAwsLexBot#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#id DataAwsLexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#version DataAwsLexBot#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexBotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
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
        if version is not None:
            self._values["version"] = version

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#name DataAwsLexBot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#id DataAwsLexBot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_bot#version DataAwsLexBot#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLexBotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLexIntent(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexIntent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/lex_intent aws_lex_intent}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/lex_intent aws_lex_intent} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#name DataAwsLexIntent#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#id DataAwsLexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#version DataAwsLexIntent#version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexIntent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsLexIntentConfig(
            name=name,
            id=id,
            version=version,
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

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignature")
    def parent_intent_signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentIntentSignature"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexIntent, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexIntent, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexIntent, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexIntentConfig",
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
        "version": "version",
    },
)
class DataAwsLexIntentConfig(cdktf.TerraformMetaArguments):
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
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#name DataAwsLexIntent#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#id DataAwsLexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#version DataAwsLexIntent#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexIntentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
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
        if version is not None:
            self._values["version"] = version

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#name DataAwsLexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#id DataAwsLexIntent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_intent#version DataAwsLexIntent#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLexIntentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLexSlotType(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexSlotType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type aws_lex_slot_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type aws_lex_slot_type} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#name DataAwsLexSlotType#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#id DataAwsLexSlotType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#version DataAwsLexSlotType#version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexSlotType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsLexSlotTypeConfig(
            name=name,
            id=id,
            version=version,
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

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="enumerationValue")
    def enumeration_value(self) -> "DataAwsLexSlotTypeEnumerationValueList":
        return typing.cast("DataAwsLexSlotTypeEnumerationValueList", jsii.get(self, "enumerationValue"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="valueSelectionStrategy")
    def value_selection_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueSelectionStrategy"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotType, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotType, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotType, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexSlotTypeConfig",
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
        "version": "version",
    },
)
class DataAwsLexSlotTypeConfig(cdktf.TerraformMetaArguments):
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
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#name DataAwsLexSlotType#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#id DataAwsLexSlotType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#version DataAwsLexSlotType#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexSlotTypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
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
        if version is not None:
            self._values["version"] = version

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#name DataAwsLexSlotType#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#id DataAwsLexSlotType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lex_slot_type#version DataAwsLexSlotType#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLexSlotTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexSlotTypeEnumerationValue",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsLexSlotTypeEnumerationValue:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLexSlotTypeEnumerationValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLexSlotTypeEnumerationValueList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexSlotTypeEnumerationValueList",
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
            type_hints = typing.get_type_hints(DataAwsLexSlotTypeEnumerationValueList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsLexSlotTypeEnumerationValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsLexSlotTypeEnumerationValueList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsLexSlotTypeEnumerationValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotTypeEnumerationValueList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotTypeEnumerationValueList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotTypeEnumerationValueList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsLexSlotTypeEnumerationValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.DataAwsLexSlotTypeEnumerationValueOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsLexSlotTypeEnumerationValueOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="synonyms")
    def synonyms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "synonyms"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsLexSlotTypeEnumerationValue]:
        return typing.cast(typing.Optional[DataAwsLexSlotTypeEnumerationValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLexSlotTypeEnumerationValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsLexSlotTypeEnumerationValueOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBot(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_bot aws_lex_bot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        abort_statement: typing.Union["LexBotAbortStatement", typing.Dict[str, typing.Any]],
        child_directed: typing.Union[builtins.bool, cdktf.IResolvable],
        intent: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        clarification_prompt: typing.Optional[typing.Union["LexBotClarificationPrompt", typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        detect_sentiment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_model_improvements: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        locale: typing.Optional[builtins.str] = None,
        nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
        process_behavior: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotTimeouts", typing.Dict[str, typing.Any]]] = None,
        voice_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_bot aws_lex_bot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param abort_statement: abort_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        :param child_directed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.
        :param intent: intent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.
        :param clarification_prompt: clarification_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.
        :param detect_sentiment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.
        :param enable_model_improvements: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_session_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.
        :param nlu_intent_confidence_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.
        :param process_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        :param voice_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexBotConfig(
            abort_statement=abort_statement,
            child_directed=child_directed,
            intent=intent,
            name=name,
            clarification_prompt=clarification_prompt,
            create_version=create_version,
            description=description,
            detect_sentiment=detect_sentiment,
            enable_model_improvements=enable_model_improvements,
            id=id,
            idle_session_ttl_in_seconds=idle_session_ttl_in_seconds,
            locale=locale,
            nlu_intent_confidence_threshold=nlu_intent_confidence_threshold,
            process_behavior=process_behavior,
            timeouts=timeouts,
            voice_id=voice_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAbortStatement")
    def put_abort_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotAbortStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        value = LexBotAbortStatement(message=message, response_card=response_card)

        return typing.cast(None, jsii.invoke(self, "putAbortStatement", [value]))

    @jsii.member(jsii_name="putClarificationPrompt")
    def put_clarification_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotClarificationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        value = LexBotClarificationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putClarificationPrompt", [value]))

    @jsii.member(jsii_name="putIntent")
    def put_intent(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBot.put_intent)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIntent", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.
        '''
        value = LexBotTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetClarificationPrompt")
    def reset_clarification_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClarificationPrompt", []))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDetectSentiment")
    def reset_detect_sentiment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetectSentiment", []))

    @jsii.member(jsii_name="resetEnableModelImprovements")
    def reset_enable_model_improvements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableModelImprovements", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleSessionTtlInSeconds")
    def reset_idle_session_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleSessionTtlInSeconds", []))

    @jsii.member(jsii_name="resetLocale")
    def reset_locale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocale", []))

    @jsii.member(jsii_name="resetNluIntentConfidenceThreshold")
    def reset_nlu_intent_confidence_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNluIntentConfidenceThreshold", []))

    @jsii.member(jsii_name="resetProcessBehavior")
    def reset_process_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessBehavior", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVoiceId")
    def reset_voice_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVoiceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="abortStatement")
    def abort_statement(self) -> "LexBotAbortStatementOutputReference":
        return typing.cast("LexBotAbortStatementOutputReference", jsii.get(self, "abortStatement"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="clarificationPrompt")
    def clarification_prompt(self) -> "LexBotClarificationPromptOutputReference":
        return typing.cast("LexBotClarificationPromptOutputReference", jsii.get(self, "clarificationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureReason"))

    @builtins.property
    @jsii.member(jsii_name="intent")
    def intent(self) -> "LexBotIntentList":
        return typing.cast("LexBotIntentList", jsii.get(self, "intent"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexBotTimeoutsOutputReference":
        return typing.cast("LexBotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="abortStatementInput")
    def abort_statement_input(self) -> typing.Optional["LexBotAbortStatement"]:
        return typing.cast(typing.Optional["LexBotAbortStatement"], jsii.get(self, "abortStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="childDirectedInput")
    def child_directed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "childDirectedInput"))

    @builtins.property
    @jsii.member(jsii_name="clarificationPromptInput")
    def clarification_prompt_input(
        self,
    ) -> typing.Optional["LexBotClarificationPrompt"]:
        return typing.cast(typing.Optional["LexBotClarificationPrompt"], jsii.get(self, "clarificationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersionInput")
    def create_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="detectSentimentInput")
    def detect_sentiment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "detectSentimentInput"))

    @builtins.property
    @jsii.member(jsii_name="enableModelImprovementsInput")
    def enable_model_improvements_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableModelImprovementsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSecondsInput")
    def idle_session_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleSessionTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="intentInput")
    def intent_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexBotIntent"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexBotIntent"]]], jsii.get(self, "intentInput"))

    @builtins.property
    @jsii.member(jsii_name="localeInput")
    def locale_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nluIntentConfidenceThresholdInput")
    def nlu_intent_confidence_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nluIntentConfidenceThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="processBehaviorInput")
    def process_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "processBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexBotTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexBotTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="voiceIdInput")
    def voice_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "voiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="childDirected")
    def child_directed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "childDirected"))

    @child_directed.setter
    def child_directed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "child_directed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "childDirected", value)

    @builtins.property
    @jsii.member(jsii_name="createVersion")
    def create_version(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createVersion"))

    @create_version.setter
    def create_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "create_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectSentiment")
    def detect_sentiment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "detectSentiment"))

    @detect_sentiment.setter
    def detect_sentiment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "detect_sentiment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectSentiment", value)

    @builtins.property
    @jsii.member(jsii_name="enableModelImprovements")
    def enable_model_improvements(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableModelImprovements"))

    @enable_model_improvements.setter
    def enable_model_improvements(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "enable_model_improvements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableModelImprovements", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleSessionTtlInSeconds"))

    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "idle_session_ttl_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleSessionTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locale"))

    @locale.setter
    def locale(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "locale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locale", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nluIntentConfidenceThreshold"))

    @nlu_intent_confidence_threshold.setter
    def nlu_intent_confidence_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "nlu_intent_confidence_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nluIntentConfidenceThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="processBehavior")
    def process_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "processBehavior"))

    @process_behavior.setter
    def process_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "process_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="voiceId")
    def voice_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "voiceId"))

    @voice_id.setter
    def voice_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBot, "voice_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "voiceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAbortStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexBotAbortStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotAbortStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAbortStatement.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexBotAbortStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexBotAbortStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAbortStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAbortStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexBotAbortStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAbortStatementMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAbortStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotAbortStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAbortStatementMessageList",
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
            type_hints = typing.get_type_hints(LexBotAbortStatementMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexBotAbortStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAbortStatementMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotAbortStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAbortStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAbortStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAbortStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAbortStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAbortStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexBotAbortStatementMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotAbortStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotAbortStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotAbortStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAbortStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAbortStatementOutputReference",
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
            type_hints = typing.get_type_hints(LexBotAbortStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexBotAbortStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAbortStatementOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexBotAbortStatementMessageList:
        return typing.cast(LexBotAbortStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAbortStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAbortStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexBotAbortStatement]:
        return typing.cast(typing.Optional[LexBotAbortStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexBotAbortStatement]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAbortStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAlias(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAlias",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias aws_lex_bot_alias}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bot_name: builtins.str,
        bot_version: builtins.str,
        name: builtins.str,
        conversation_logs: typing.Optional[typing.Union["LexBotAliasConversationLogs", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotAliasTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias aws_lex_bot_alias} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_name LexBotAlias#bot_name}.
        :param bot_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_version LexBotAlias#bot_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#name LexBotAlias#name}.
        :param conversation_logs: conversation_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#conversation_logs LexBotAlias#conversation_logs}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#description LexBotAlias#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#id LexBotAlias#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#timeouts LexBotAlias#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAlias.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexBotAliasConfig(
            bot_name=bot_name,
            bot_version=bot_version,
            name=name,
            conversation_logs=conversation_logs,
            description=description,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConversationLogs")
    def put_conversation_logs(
        self,
        *,
        iam_role_arn: builtins.str,
        log_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotAliasConversationLogsLogSettings", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#iam_role_arn LexBotAlias#iam_role_arn}.
        :param log_settings: log_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#log_settings LexBotAlias#log_settings}
        '''
        value = LexBotAliasConversationLogs(
            iam_role_arn=iam_role_arn, log_settings=log_settings
        )

        return typing.cast(None, jsii.invoke(self, "putConversationLogs", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#create LexBotAlias#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#delete LexBotAlias#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#update LexBotAlias#update}.
        '''
        value = LexBotAliasTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConversationLogs")
    def reset_conversation_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConversationLogs", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="conversationLogs")
    def conversation_logs(self) -> "LexBotAliasConversationLogsOutputReference":
        return typing.cast("LexBotAliasConversationLogsOutputReference", jsii.get(self, "conversationLogs"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexBotAliasTimeoutsOutputReference":
        return typing.cast("LexBotAliasTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="botNameInput")
    def bot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "botNameInput"))

    @builtins.property
    @jsii.member(jsii_name="botVersionInput")
    def bot_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "botVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationLogsInput")
    def conversation_logs_input(self) -> typing.Optional["LexBotAliasConversationLogs"]:
        return typing.cast(typing.Optional["LexBotAliasConversationLogs"], jsii.get(self, "conversationLogsInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexBotAliasTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexBotAliasTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="botName")
    def bot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "botName"))

    @bot_name.setter
    def bot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAlias, "bot_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botName", value)

    @builtins.property
    @jsii.member(jsii_name="botVersion")
    def bot_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "botVersion"))

    @bot_version.setter
    def bot_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAlias, "bot_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAlias, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAlias, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAlias, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bot_name": "botName",
        "bot_version": "botVersion",
        "name": "name",
        "conversation_logs": "conversationLogs",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class LexBotAliasConfig(cdktf.TerraformMetaArguments):
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
        bot_name: builtins.str,
        bot_version: builtins.str,
        name: builtins.str,
        conversation_logs: typing.Optional[typing.Union["LexBotAliasConversationLogs", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotAliasTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_name LexBotAlias#bot_name}.
        :param bot_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_version LexBotAlias#bot_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#name LexBotAlias#name}.
        :param conversation_logs: conversation_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#conversation_logs LexBotAlias#conversation_logs}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#description LexBotAlias#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#id LexBotAlias#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#timeouts LexBotAlias#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(conversation_logs, dict):
            conversation_logs = LexBotAliasConversationLogs(**conversation_logs)
        if isinstance(timeouts, dict):
            timeouts = LexBotAliasTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bot_name", value=bot_name, expected_type=type_hints["bot_name"])
            check_type(argname="argument bot_version", value=bot_version, expected_type=type_hints["bot_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument conversation_logs", value=conversation_logs, expected_type=type_hints["conversation_logs"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "bot_name": bot_name,
            "bot_version": bot_version,
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
        if conversation_logs is not None:
            self._values["conversation_logs"] = conversation_logs
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def bot_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_name LexBotAlias#bot_name}.'''
        result = self._values.get("bot_name")
        assert result is not None, "Required property 'bot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#bot_version LexBotAlias#bot_version}.'''
        result = self._values.get("bot_version")
        assert result is not None, "Required property 'bot_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#name LexBotAlias#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conversation_logs(self) -> typing.Optional["LexBotAliasConversationLogs"]:
        '''conversation_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#conversation_logs LexBotAlias#conversation_logs}
        '''
        result = self._values.get("conversation_logs")
        return typing.cast(typing.Optional["LexBotAliasConversationLogs"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#description LexBotAlias#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#id LexBotAlias#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexBotAliasTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#timeouts LexBotAlias#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexBotAliasTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAliasConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConversationLogs",
    jsii_struct_bases=[],
    name_mapping={"iam_role_arn": "iamRoleArn", "log_settings": "logSettings"},
)
class LexBotAliasConversationLogs:
    def __init__(
        self,
        *,
        iam_role_arn: builtins.str,
        log_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotAliasConversationLogsLogSettings", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#iam_role_arn LexBotAlias#iam_role_arn}.
        :param log_settings: log_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#log_settings LexBotAlias#log_settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasConversationLogs.__init__)
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument log_settings", value=log_settings, expected_type=type_hints["log_settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "iam_role_arn": iam_role_arn,
        }
        if log_settings is not None:
            self._values["log_settings"] = log_settings

    @builtins.property
    def iam_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#iam_role_arn LexBotAlias#iam_role_arn}.'''
        result = self._values.get("iam_role_arn")
        assert result is not None, "Required property 'iam_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_settings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexBotAliasConversationLogsLogSettings"]]]:
        '''log_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#log_settings LexBotAlias#log_settings}
        '''
        result = self._values.get("log_settings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexBotAliasConversationLogsLogSettings"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAliasConversationLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConversationLogsLogSettings",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "log_type": "logType",
        "resource_arn": "resourceArn",
        "kms_key_arn": "kmsKeyArn",
    },
)
class LexBotAliasConversationLogsLogSettings:
    def __init__(
        self,
        *,
        destination: builtins.str,
        log_type: builtins.str,
        resource_arn: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#destination LexBotAlias#destination}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#log_type LexBotAlias#log_type}.
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#resource_arn LexBotAlias#resource_arn}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#kms_key_arn LexBotAlias#kms_key_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsLogSettings.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "log_type": log_type,
            "resource_arn": resource_arn,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#destination LexBotAlias#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#log_type LexBotAlias#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#resource_arn LexBotAlias#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#kms_key_arn LexBotAlias#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAliasConversationLogsLogSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotAliasConversationLogsLogSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConversationLogsLogSettingsList",
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
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsLogSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexBotAliasConversationLogsLogSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsLogSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotAliasConversationLogsLogSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAliasConversationLogsLogSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAliasConversationLogsLogSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAliasConversationLogsLogSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAliasConversationLogsLogSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConversationLogsLogSettingsOutputReference",
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
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsLogSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="resourcePrefix")
    def resource_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourcePrefix"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsOutputReference, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsOutputReference, "log_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsOutputReference, "resource_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotAliasConversationLogsLogSettings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotAliasConversationLogsLogSettings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotAliasConversationLogsLogSettings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsLogSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotAliasConversationLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasConversationLogsOutputReference",
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
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogSettings")
    def put_log_settings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexBotAliasConversationLogsLogSettings, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasConversationLogsOutputReference.put_log_settings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogSettings", [value]))

    @jsii.member(jsii_name="resetLogSettings")
    def reset_log_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogSettings", []))

    @builtins.property
    @jsii.member(jsii_name="logSettings")
    def log_settings(self) -> LexBotAliasConversationLogsLogSettingsList:
        return typing.cast(LexBotAliasConversationLogsLogSettingsList, jsii.get(self, "logSettings"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleArnInput")
    def iam_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logSettingsInput")
    def log_settings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAliasConversationLogsLogSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotAliasConversationLogsLogSettings]]], jsii.get(self, "logSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsOutputReference, "iam_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexBotAliasConversationLogs]:
        return typing.cast(typing.Optional[LexBotAliasConversationLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexBotAliasConversationLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasConversationLogsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexBotAliasTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#create LexBotAlias#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#delete LexBotAlias#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#update LexBotAlias#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotAliasTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#create LexBotAlias#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#delete LexBotAlias#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot_alias#update LexBotAlias#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotAliasTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotAliasTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotAliasTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LexBotAliasTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotAliasTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotAliasTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotAliasTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotAliasTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotClarificationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexBotClarificationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotClarificationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotClarificationPrompt.__init__)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#max_attempts LexBot#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexBotClarificationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#message LexBot#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexBotClarificationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#response_card LexBot#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotClarificationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotClarificationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexBotClarificationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotClarificationPromptMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content LexBot#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#content_type LexBot#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#group_number LexBot#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotClarificationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotClarificationPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotClarificationPromptMessageList",
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
            type_hints = typing.get_type_hints(LexBotClarificationPromptMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexBotClarificationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotClarificationPromptMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotClarificationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotClarificationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotClarificationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotClarificationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotClarificationPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotClarificationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexBotClarificationPromptMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotClarificationPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotClarificationPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotClarificationPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotClarificationPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotClarificationPromptOutputReference",
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
            type_hints = typing.get_type_hints(LexBotClarificationPromptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexBotClarificationPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotClarificationPromptOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexBotClarificationPromptMessageList:
        return typing.cast(LexBotClarificationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotClarificationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotClarificationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptOutputReference, "max_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexBotClarificationPrompt]:
        return typing.cast(typing.Optional[LexBotClarificationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexBotClarificationPrompt]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotClarificationPromptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "abort_statement": "abortStatement",
        "child_directed": "childDirected",
        "intent": "intent",
        "name": "name",
        "clarification_prompt": "clarificationPrompt",
        "create_version": "createVersion",
        "description": "description",
        "detect_sentiment": "detectSentiment",
        "enable_model_improvements": "enableModelImprovements",
        "id": "id",
        "idle_session_ttl_in_seconds": "idleSessionTtlInSeconds",
        "locale": "locale",
        "nlu_intent_confidence_threshold": "nluIntentConfidenceThreshold",
        "process_behavior": "processBehavior",
        "timeouts": "timeouts",
        "voice_id": "voiceId",
    },
)
class LexBotConfig(cdktf.TerraformMetaArguments):
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
        abort_statement: typing.Union[LexBotAbortStatement, typing.Dict[str, typing.Any]],
        child_directed: typing.Union[builtins.bool, cdktf.IResolvable],
        intent: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexBotIntent", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        clarification_prompt: typing.Optional[typing.Union[LexBotClarificationPrompt, typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        detect_sentiment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_model_improvements: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_session_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        locale: typing.Optional[builtins.str] = None,
        nlu_intent_confidence_threshold: typing.Optional[jsii.Number] = None,
        process_behavior: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexBotTimeouts", typing.Dict[str, typing.Any]]] = None,
        voice_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param abort_statement: abort_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        :param child_directed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.
        :param intent: intent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.
        :param clarification_prompt: clarification_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.
        :param detect_sentiment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.
        :param enable_model_improvements: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_session_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.
        :param locale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.
        :param nlu_intent_confidence_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.
        :param process_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        :param voice_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(abort_statement, dict):
            abort_statement = LexBotAbortStatement(**abort_statement)
        if isinstance(clarification_prompt, dict):
            clarification_prompt = LexBotClarificationPrompt(**clarification_prompt)
        if isinstance(timeouts, dict):
            timeouts = LexBotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LexBotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument abort_statement", value=abort_statement, expected_type=type_hints["abort_statement"])
            check_type(argname="argument child_directed", value=child_directed, expected_type=type_hints["child_directed"])
            check_type(argname="argument intent", value=intent, expected_type=type_hints["intent"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument clarification_prompt", value=clarification_prompt, expected_type=type_hints["clarification_prompt"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument detect_sentiment", value=detect_sentiment, expected_type=type_hints["detect_sentiment"])
            check_type(argname="argument enable_model_improvements", value=enable_model_improvements, expected_type=type_hints["enable_model_improvements"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_session_ttl_in_seconds", value=idle_session_ttl_in_seconds, expected_type=type_hints["idle_session_ttl_in_seconds"])
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument nlu_intent_confidence_threshold", value=nlu_intent_confidence_threshold, expected_type=type_hints["nlu_intent_confidence_threshold"])
            check_type(argname="argument process_behavior", value=process_behavior, expected_type=type_hints["process_behavior"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument voice_id", value=voice_id, expected_type=type_hints["voice_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "abort_statement": abort_statement,
            "child_directed": child_directed,
            "intent": intent,
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
        if clarification_prompt is not None:
            self._values["clarification_prompt"] = clarification_prompt
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if detect_sentiment is not None:
            self._values["detect_sentiment"] = detect_sentiment
        if enable_model_improvements is not None:
            self._values["enable_model_improvements"] = enable_model_improvements
        if id is not None:
            self._values["id"] = id
        if idle_session_ttl_in_seconds is not None:
            self._values["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if locale is not None:
            self._values["locale"] = locale
        if nlu_intent_confidence_threshold is not None:
            self._values["nlu_intent_confidence_threshold"] = nlu_intent_confidence_threshold
        if process_behavior is not None:
            self._values["process_behavior"] = process_behavior
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if voice_id is not None:
            self._values["voice_id"] = voice_id

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
    def abort_statement(self) -> LexBotAbortStatement:
        '''abort_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#abort_statement LexBot#abort_statement}
        '''
        result = self._values.get("abort_statement")
        assert result is not None, "Required property 'abort_statement' is missing"
        return typing.cast(LexBotAbortStatement, result)

    @builtins.property
    def child_directed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#child_directed LexBot#child_directed}.'''
        result = self._values.get("child_directed")
        assert result is not None, "Required property 'child_directed' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def intent(self) -> typing.Union[cdktf.IResolvable, typing.List["LexBotIntent"]]:
        '''intent block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent LexBot#intent}
        '''
        result = self._values.get("intent")
        assert result is not None, "Required property 'intent' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexBotIntent"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#name LexBot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clarification_prompt(self) -> typing.Optional[LexBotClarificationPrompt]:
        '''clarification_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#clarification_prompt LexBot#clarification_prompt}
        '''
        result = self._values.get("clarification_prompt")
        return typing.cast(typing.Optional[LexBotClarificationPrompt], result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create_version LexBot#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#description LexBot#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detect_sentiment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#detect_sentiment LexBot#detect_sentiment}.'''
        result = self._values.get("detect_sentiment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_model_improvements(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#enable_model_improvements LexBot#enable_model_improvements}.'''
        result = self._values.get("enable_model_improvements")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#id LexBot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_session_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#idle_session_ttl_in_seconds LexBot#idle_session_ttl_in_seconds}.'''
        result = self._values.get("idle_session_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def locale(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#locale LexBot#locale}.'''
        result = self._values.get("locale")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nlu_intent_confidence_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#nlu_intent_confidence_threshold LexBot#nlu_intent_confidence_threshold}.'''
        result = self._values.get("nlu_intent_confidence_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def process_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#process_behavior LexBot#process_behavior}.'''
        result = self._values.get("process_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexBotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#timeouts LexBot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexBotTimeouts"], result)

    @builtins.property
    def voice_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#voice_id LexBot#voice_id}.'''
        result = self._values.get("voice_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotIntent",
    jsii_struct_bases=[],
    name_mapping={"intent_name": "intentName", "intent_version": "intentVersion"},
)
class LexBotIntent:
    def __init__(
        self,
        *,
        intent_name: builtins.str,
        intent_version: builtins.str,
    ) -> None:
        '''
        :param intent_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_name LexBot#intent_name}.
        :param intent_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_version LexBot#intent_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotIntent.__init__)
            check_type(argname="argument intent_name", value=intent_name, expected_type=type_hints["intent_name"])
            check_type(argname="argument intent_version", value=intent_version, expected_type=type_hints["intent_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "intent_name": intent_name,
            "intent_version": intent_version,
        }

    @builtins.property
    def intent_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_name LexBot#intent_name}.'''
        result = self._values.get("intent_name")
        assert result is not None, "Required property 'intent_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def intent_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#intent_version LexBot#intent_version}.'''
        result = self._values.get("intent_version")
        assert result is not None, "Required property 'intent_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotIntent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotIntentList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotIntentList",
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
            type_hints = typing.get_type_hints(LexBotIntentList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexBotIntentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotIntentList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexBotIntentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotIntentList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotIntentList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexBotIntentList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotIntent]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotIntent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexBotIntent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotIntentList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexBotIntentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotIntentOutputReference",
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
            type_hints = typing.get_type_hints(LexBotIntentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="intentNameInput")
    def intent_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="intentVersionInput")
    def intent_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="intentName")
    def intent_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intentName"))

    @intent_name.setter
    def intent_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotIntentOutputReference, "intent_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intentName", value)

    @builtins.property
    @jsii.member(jsii_name="intentVersion")
    def intent_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intentVersion"))

    @intent_version.setter
    def intent_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotIntentOutputReference, "intent_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotIntent, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotIntent, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotIntent, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotIntentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexBotTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexBotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexBotTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#create LexBot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#delete LexBot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_bot#update LexBot#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexBotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexBotTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexBotTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LexBotTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexBotTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexBotTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexBotTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexBotTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntent(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union["LexIntentConclusionStatement", typing.Dict[str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexIntentConfig(
            fulfillment_activity=fulfillment_activity,
            name=name,
            conclusion_statement=conclusion_statement,
            confirmation_prompt=confirmation_prompt,
            create_version=create_version,
            description=description,
            dialog_code_hook=dialog_code_hook,
            follow_up_prompt=follow_up_prompt,
            id=id,
            parent_intent_signature=parent_intent_signature,
            rejection_statement=rejection_statement,
            sample_utterances=sample_utterances,
            slot=slot,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConclusionStatement")
    def put_conclusion_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConclusionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConclusionStatement", [value]))

    @jsii.member(jsii_name="putConfirmationPrompt")
    def put_confirmation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConfirmationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConfirmationPrompt", [value]))

    @jsii.member(jsii_name="putDialogCodeHook")
    def put_dialog_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentDialogCodeHook(message_version=message_version, uri=uri)

        return typing.cast(None, jsii.invoke(self, "putDialogCodeHook", [value]))

    @jsii.member(jsii_name="putFollowUpPrompt")
    def put_follow_up_prompt(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        value = LexIntentFollowUpPrompt(
            prompt=prompt, rejection_statement=rejection_statement
        )

        return typing.cast(None, jsii.invoke(self, "putFollowUpPrompt", [value]))

    @jsii.member(jsii_name="putFulfillmentActivity")
    def put_fulfillment_activity(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        value = LexIntentFulfillmentActivity(type=type, code_hook=code_hook)

        return typing.cast(None, jsii.invoke(self, "putFulfillmentActivity", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @jsii.member(jsii_name="putSlot")
    def put_slot(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntent.put_slot)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlot", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        value = LexIntentTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConclusionStatement")
    def reset_conclusion_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConclusionStatement", []))

    @jsii.member(jsii_name="resetConfirmationPrompt")
    def reset_confirmation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationPrompt", []))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDialogCodeHook")
    def reset_dialog_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDialogCodeHook", []))

    @jsii.member(jsii_name="resetFollowUpPrompt")
    def reset_follow_up_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowUpPrompt", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParentIntentSignature")
    def reset_parent_intent_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentIntentSignature", []))

    @jsii.member(jsii_name="resetRejectionStatement")
    def reset_rejection_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectionStatement", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlot")
    def reset_slot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlot", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatement")
    def conclusion_statement(self) -> "LexIntentConclusionStatementOutputReference":
        return typing.cast("LexIntentConclusionStatementOutputReference", jsii.get(self, "conclusionStatement"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPrompt")
    def confirmation_prompt(self) -> "LexIntentConfirmationPromptOutputReference":
        return typing.cast("LexIntentConfirmationPromptOutputReference", jsii.get(self, "confirmationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="dialogCodeHook")
    def dialog_code_hook(self) -> "LexIntentDialogCodeHookOutputReference":
        return typing.cast("LexIntentDialogCodeHookOutputReference", jsii.get(self, "dialogCodeHook"))

    @builtins.property
    @jsii.member(jsii_name="followUpPrompt")
    def follow_up_prompt(self) -> "LexIntentFollowUpPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptOutputReference", jsii.get(self, "followUpPrompt"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivity")
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivityOutputReference":
        return typing.cast("LexIntentFulfillmentActivityOutputReference", jsii.get(self, "fulfillmentActivity"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(self) -> "LexIntentRejectionStatementOutputReference":
        return typing.cast("LexIntentRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="slot")
    def slot(self) -> "LexIntentSlotList":
        return typing.cast("LexIntentSlotList", jsii.get(self, "slot"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexIntentTimeoutsOutputReference":
        return typing.cast("LexIntentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatementInput")
    def conclusion_statement_input(
        self,
    ) -> typing.Optional["LexIntentConclusionStatement"]:
        return typing.cast(typing.Optional["LexIntentConclusionStatement"], jsii.get(self, "conclusionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPromptInput")
    def confirmation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentConfirmationPrompt"]:
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], jsii.get(self, "confirmationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersionInput")
    def create_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dialogCodeHookInput")
    def dialog_code_hook_input(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], jsii.get(self, "dialogCodeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="followUpPromptInput")
    def follow_up_prompt_input(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], jsii.get(self, "followUpPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivityInput")
    def fulfillment_activity_input(
        self,
    ) -> typing.Optional["LexIntentFulfillmentActivity"]:
        return typing.cast(typing.Optional["LexIntentFulfillmentActivity"], jsii.get(self, "fulfillmentActivityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignatureInput")
    def parent_intent_signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentIntentSignatureInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotInput")
    def slot_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]], jsii.get(self, "slotInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexIntentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexIntentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersion")
    def create_version(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createVersion"))

    @create_version.setter
    def create_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "create_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignature")
    def parent_intent_signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentIntentSignature"))

    @parent_intent_signature.setter
    def parent_intent_signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "parent_intent_signature").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentIntentSignature", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntent, "sample_utterances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentConclusionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentConclusionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConclusionStatement.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentConclusionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentConclusionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentConclusionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConclusionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConclusionStatementMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConclusionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConclusionStatementMessageList",
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
            type_hints = typing.get_type_hints(LexIntentConclusionStatementMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentConclusionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConclusionStatementMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConclusionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConclusionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentConclusionStatementMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConclusionStatementOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentConclusionStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConclusionStatementOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConclusionStatementMessageList:
        return typing.cast(LexIntentConclusionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConclusionStatement]:
        return typing.cast(typing.Optional[LexIntentConclusionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConclusionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConclusionStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "fulfillment_activity": "fulfillmentActivity",
        "name": "name",
        "conclusion_statement": "conclusionStatement",
        "confirmation_prompt": "confirmationPrompt",
        "create_version": "createVersion",
        "description": "description",
        "dialog_code_hook": "dialogCodeHook",
        "follow_up_prompt": "followUpPrompt",
        "id": "id",
        "parent_intent_signature": "parentIntentSignature",
        "rejection_statement": "rejectionStatement",
        "sample_utterances": "sampleUtterances",
        "slot": "slot",
        "timeouts": "timeouts",
    },
)
class LexIntentConfig(cdktf.TerraformMetaArguments):
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
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(fulfillment_activity, dict):
            fulfillment_activity = LexIntentFulfillmentActivity(**fulfillment_activity)
        if isinstance(conclusion_statement, dict):
            conclusion_statement = LexIntentConclusionStatement(**conclusion_statement)
        if isinstance(confirmation_prompt, dict):
            confirmation_prompt = LexIntentConfirmationPrompt(**confirmation_prompt)
        if isinstance(dialog_code_hook, dict):
            dialog_code_hook = LexIntentDialogCodeHook(**dialog_code_hook)
        if isinstance(follow_up_prompt, dict):
            follow_up_prompt = LexIntentFollowUpPrompt(**follow_up_prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentRejectionStatement(**rejection_statement)
        if isinstance(timeouts, dict):
            timeouts = LexIntentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument fulfillment_activity", value=fulfillment_activity, expected_type=type_hints["fulfillment_activity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument conclusion_statement", value=conclusion_statement, expected_type=type_hints["conclusion_statement"])
            check_type(argname="argument confirmation_prompt", value=confirmation_prompt, expected_type=type_hints["confirmation_prompt"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dialog_code_hook", value=dialog_code_hook, expected_type=type_hints["dialog_code_hook"])
            check_type(argname="argument follow_up_prompt", value=follow_up_prompt, expected_type=type_hints["follow_up_prompt"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent_intent_signature", value=parent_intent_signature, expected_type=type_hints["parent_intent_signature"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot", value=slot, expected_type=type_hints["slot"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "fulfillment_activity": fulfillment_activity,
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
        if conclusion_statement is not None:
            self._values["conclusion_statement"] = conclusion_statement
        if confirmation_prompt is not None:
            self._values["confirmation_prompt"] = confirmation_prompt
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if dialog_code_hook is not None:
            self._values["dialog_code_hook"] = dialog_code_hook
        if follow_up_prompt is not None:
            self._values["follow_up_prompt"] = follow_up_prompt
        if id is not None:
            self._values["id"] = id
        if parent_intent_signature is not None:
            self._values["parent_intent_signature"] = parent_intent_signature
        if rejection_statement is not None:
            self._values["rejection_statement"] = rejection_statement
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot is not None:
            self._values["slot"] = slot
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivity":
        '''fulfillment_activity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        '''
        result = self._values.get("fulfillment_activity")
        assert result is not None, "Required property 'fulfillment_activity' is missing"
        return typing.cast("LexIntentFulfillmentActivity", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conclusion_statement(self) -> typing.Optional[LexIntentConclusionStatement]:
        '''conclusion_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        '''
        result = self._values.get("conclusion_statement")
        return typing.cast(typing.Optional[LexIntentConclusionStatement], result)

    @builtins.property
    def confirmation_prompt(self) -> typing.Optional["LexIntentConfirmationPrompt"]:
        '''confirmation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        '''
        result = self._values.get("confirmation_prompt")
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dialog_code_hook(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        '''dialog_code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        '''
        result = self._values.get("dialog_code_hook")
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], result)

    @builtins.property
    def follow_up_prompt(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        '''follow_up_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        '''
        result = self._values.get("follow_up_prompt")
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_intent_signature(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.'''
        result = self._values.get("parent_intent_signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rejection_statement(self) -> typing.Optional["LexIntentRejectionStatement"]:
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]]:
        '''slot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        '''
        result = self._values.get("slot")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexIntentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexIntentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfirmationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentConfirmationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConfirmationPrompt.__init__)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfirmationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConfirmationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConfirmationPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfirmationPromptMessageList",
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
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentConfirmationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConfirmationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfirmationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentConfirmationPromptOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentConfirmationPromptOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConfirmationPromptMessageList:
        return typing.cast(LexIntentConfirmationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptOutputReference, "max_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConfirmationPrompt]:
        return typing.cast(typing.Optional[LexIntentConfirmationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConfirmationPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentConfirmationPromptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentDialogCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentDialogCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentDialogCodeHook.__init__)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentDialogCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentDialogCodeHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentDialogCodeHookOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentDialogCodeHookOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentDialogCodeHookOutputReference, "message_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentDialogCodeHookOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentDialogCodeHook]:
        return typing.cast(typing.Optional[LexIntentDialogCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentDialogCodeHook]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentDialogCodeHookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPrompt",
    jsii_struct_bases=[],
    name_mapping={"prompt": "prompt", "rejection_statement": "rejectionStatement"},
)
class LexIntentFollowUpPrompt:
    def __init__(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        if isinstance(prompt, dict):
            prompt = LexIntentFollowUpPromptPrompt(**prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentFollowUpPromptRejectionStatement(**rejection_statement)
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPrompt.__init__)
            check_type(argname="argument prompt", value=prompt, expected_type=type_hints["prompt"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "prompt": prompt,
            "rejection_statement": rejection_statement,
        }

    @builtins.property
    def prompt(self) -> "LexIntentFollowUpPromptPrompt":
        '''prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        '''
        result = self._values.get("prompt")
        assert result is not None, "Required property 'prompt' is missing"
        return typing.cast("LexIntentFollowUpPromptPrompt", result)

    @builtins.property
    def rejection_statement(self) -> "LexIntentFollowUpPromptRejectionStatement":
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        assert result is not None, "Required property 'rejection_statement' is missing"
        return typing.cast("LexIntentFollowUpPromptRejectionStatement", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPrompt")
    def put_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putPrompt", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="prompt")
    def prompt(self) -> "LexIntentFollowUpPromptPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptPromptOutputReference", jsii.get(self, "prompt"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> "LexIntentFollowUpPromptRejectionStatementOutputReference":
        return typing.cast("LexIntentFollowUpPromptRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="promptInput")
    def prompt_input(self) -> typing.Optional["LexIntentFollowUpPromptPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptPrompt"], jsii.get(self, "promptInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentFollowUpPromptRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentFollowUpPrompt]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentFollowUpPromptPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPrompt.__init__)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptPromptMessageList",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentFollowUpPromptPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptPromptOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptPromptOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptPromptMessageList:
        return typing.cast(LexIntentFollowUpPromptPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptOutputReference, "max_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPromptPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptPromptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentFollowUpPromptRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatement.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptRejectionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptRejectionStatementMessageList",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentFollowUpPromptRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFollowUpPromptRejectionStatementOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFollowUpPromptRejectionStatementOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptRejectionStatementMessageList:
        return typing.cast(LexIntentFollowUpPromptRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LexIntentFollowUpPromptRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptRejectionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFollowUpPromptRejectionStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFulfillmentActivity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "code_hook": "codeHook"},
)
class LexIntentFulfillmentActivity:
    def __init__(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        if isinstance(code_hook, dict):
            code_hook = LexIntentFulfillmentActivityCodeHook(**code_hook)
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFulfillmentActivity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if code_hook is not None:
            self._values["code_hook"] = code_hook

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_hook(self) -> typing.Optional["LexIntentFulfillmentActivityCodeHook"]:
        '''code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        result = self._values.get("code_hook")
        return typing.cast(typing.Optional["LexIntentFulfillmentActivityCodeHook"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentFulfillmentActivityCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentFulfillmentActivityCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentFulfillmentActivityCodeHook.__init__)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivityCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFulfillmentActivityCodeHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFulfillmentActivityCodeHookOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFulfillmentActivityCodeHookOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFulfillmentActivityCodeHookOutputReference, "message_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFulfillmentActivityCodeHookOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivityCodeHook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFulfillmentActivityCodeHookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFulfillmentActivityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentFulfillmentActivityOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentFulfillmentActivityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeHook")
    def put_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentFulfillmentActivityCodeHook(
            message_version=message_version, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putCodeHook", [value]))

    @jsii.member(jsii_name="resetCodeHook")
    def reset_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeHook", []))

    @builtins.property
    @jsii.member(jsii_name="codeHook")
    def code_hook(self) -> LexIntentFulfillmentActivityCodeHookOutputReference:
        return typing.cast(LexIntentFulfillmentActivityCodeHookOutputReference, jsii.get(self, "codeHook"))

    @builtins.property
    @jsii.member(jsii_name="codeHookInput")
    def code_hook_input(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "codeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFulfillmentActivityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivity]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentFulfillmentActivityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentRejectionStatement.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentRejectionStatementMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentRejectionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentRejectionStatementMessageList",
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
            type_hints = typing.get_type_hints(LexIntentRejectionStatementMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentRejectionStatementMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentRejectionStatementMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentRejectionStatementMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentRejectionStatementOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentRejectionStatementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentRejectionStatementOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentRejectionStatementMessageList:
        return typing.cast(LexIntentRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentRejectionStatement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentRejectionStatementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlot",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "slot_constraint": "slotConstraint",
        "slot_type": "slotType",
        "description": "description",
        "priority": "priority",
        "response_card": "responseCard",
        "sample_utterances": "sampleUtterances",
        "slot_type_version": "slotTypeVersion",
        "value_elicitation_prompt": "valueElicitationPrompt",
    },
)
class LexIntentSlot:
    def __init__(
        self,
        *,
        name: builtins.str,
        slot_constraint: builtins.str,
        slot_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        response_card: typing.Optional[builtins.str] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot_type_version: typing.Optional[builtins.str] = None,
        value_elicitation_prompt: typing.Optional[typing.Union["LexIntentSlotValueElicitationPrompt", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param slot_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.
        :param slot_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot_type_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.
        :param value_elicitation_prompt: value_elicitation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        if isinstance(value_elicitation_prompt, dict):
            value_elicitation_prompt = LexIntentSlotValueElicitationPrompt(**value_elicitation_prompt)
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlot.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument slot_constraint", value=slot_constraint, expected_type=type_hints["slot_constraint"])
            check_type(argname="argument slot_type", value=slot_type, expected_type=type_hints["slot_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot_type_version", value=slot_type_version, expected_type=type_hints["slot_type_version"])
            check_type(argname="argument value_elicitation_prompt", value=value_elicitation_prompt, expected_type=type_hints["value_elicitation_prompt"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "slot_constraint": slot_constraint,
            "slot_type": slot_type,
        }
        if description is not None:
            self._values["description"] = description
        if priority is not None:
            self._values["priority"] = priority
        if response_card is not None:
            self._values["response_card"] = response_card
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot_type_version is not None:
            self._values["slot_type_version"] = slot_type_version
        if value_elicitation_prompt is not None:
            self._values["value_elicitation_prompt"] = value_elicitation_prompt

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_constraint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.'''
        result = self._values.get("slot_constraint")
        assert result is not None, "Required property 'slot_constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.'''
        result = self._values.get("slot_type")
        assert result is not None, "Required property 'slot_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot_type_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.'''
        result = self._values.get("slot_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_elicitation_prompt(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        '''value_elicitation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        result = self._values.get("value_elicitation_prompt")
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotList",
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
            type_hints = typing.get_type_hints(LexIntentSlotList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexIntentSlotOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlotList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentSlotList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentSlotList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentSlotOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValueElicitationPrompt")
    def put_value_elicitation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentSlotValueElicitationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putValueElicitationPrompt", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlotTypeVersion")
    def reset_slot_type_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlotTypeVersion", []))

    @jsii.member(jsii_name="resetValueElicitationPrompt")
    def reset_value_elicitation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueElicitationPrompt", []))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPrompt")
    def value_elicitation_prompt(
        self,
    ) -> "LexIntentSlotValueElicitationPromptOutputReference":
        return typing.cast("LexIntentSlotValueElicitationPromptOutputReference", jsii.get(self, "valueElicitationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotConstraintInput")
    def slot_constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeInput")
    def slot_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersionInput")
    def slot_type_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPromptInput")
    def value_elicitation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], jsii.get(self, "valueElicitationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "sample_utterances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)

    @builtins.property
    @jsii.member(jsii_name="slotConstraint")
    def slot_constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotConstraint"))

    @slot_constraint.setter
    def slot_constraint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "slot_constraint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="slotType")
    def slot_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotType"))

    @slot_type.setter
    def slot_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "slot_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotType", value)

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersion")
    def slot_type_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotTypeVersion"))

    @slot_type_version.setter
    def slot_type_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "slot_type_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotValueElicitationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentSlotValueElicitationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPrompt.__init__)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotValueElicitationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentSlotValueElicitationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptMessage.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotValueElicitationPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotValueElicitationPromptMessageList",
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
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptMessageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LexIntentSlotValueElicitationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptMessageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotValueElicitationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotValueElicitationPromptMessageOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptMessageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageOutputReference, "group_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptMessageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentSlotValueElicitationPromptOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentSlotValueElicitationPromptOutputReference.put_message)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentSlotValueElicitationPromptMessageList:
        return typing.cast(LexIntentSlotValueElicitationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptOutputReference, "max_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptOutputReference, "response_card").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentSlotValueElicitationPrompt]:
        return typing.cast(typing.Optional[LexIntentSlotValueElicitationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentSlotValueElicitationPrompt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentSlotValueElicitationPromptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexIntentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexIntentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexIntentTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexIntentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LexIntentTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexIntentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexSlotType(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexSlotType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type aws_lex_slot_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        enumeration_value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexSlotTypeEnumerationValue", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexSlotTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
        value_selection_strategy: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type aws_lex_slot_type} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enumeration_value: enumeration_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#enumeration_value LexSlotType#enumeration_value}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#name LexSlotType#name}.
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create_version LexSlotType#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#description LexSlotType#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#id LexSlotType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#timeouts LexSlotType#timeouts}
        :param value_selection_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#value_selection_strategy LexSlotType#value_selection_strategy}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LexSlotTypeConfig(
            enumeration_value=enumeration_value,
            name=name,
            create_version=create_version,
            description=description,
            id=id,
            timeouts=timeouts,
            value_selection_strategy=value_selection_strategy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEnumerationValue")
    def put_enumeration_value(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexSlotTypeEnumerationValue", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotType.put_enumeration_value)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnumerationValue", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create LexSlotType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#delete LexSlotType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#update LexSlotType#update}.
        '''
        value = LexSlotTypeTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetValueSelectionStrategy")
    def reset_value_selection_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueSelectionStrategy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="enumerationValue")
    def enumeration_value(self) -> "LexSlotTypeEnumerationValueList":
        return typing.cast("LexSlotTypeEnumerationValueList", jsii.get(self, "enumerationValue"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexSlotTypeTimeoutsOutputReference":
        return typing.cast("LexSlotTypeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="createVersionInput")
    def create_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enumerationValueInput")
    def enumeration_value_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexSlotTypeEnumerationValue"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexSlotTypeEnumerationValue"]]], jsii.get(self, "enumerationValueInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexSlotTypeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexSlotTypeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueSelectionStrategyInput")
    def value_selection_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueSelectionStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersion")
    def create_version(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createVersion"))

    @create_version.setter
    def create_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotType, "create_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotType, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotType, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotType, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="valueSelectionStrategy")
    def value_selection_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueSelectionStrategy"))

    @value_selection_strategy.setter
    def value_selection_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotType, "value_selection_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueSelectionStrategy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enumeration_value": "enumerationValue",
        "name": "name",
        "create_version": "createVersion",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
        "value_selection_strategy": "valueSelectionStrategy",
    },
)
class LexSlotTypeConfig(cdktf.TerraformMetaArguments):
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
        enumeration_value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexSlotTypeEnumerationValue", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LexSlotTypeTimeouts", typing.Dict[str, typing.Any]]] = None,
        value_selection_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Lex.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param enumeration_value: enumeration_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#enumeration_value LexSlotType#enumeration_value}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#name LexSlotType#name}.
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create_version LexSlotType#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#description LexSlotType#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#id LexSlotType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#timeouts LexSlotType#timeouts}
        :param value_selection_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#value_selection_strategy LexSlotType#value_selection_strategy}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = LexSlotTypeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotTypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enumeration_value", value=enumeration_value, expected_type=type_hints["enumeration_value"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument value_selection_strategy", value=value_selection_strategy, expected_type=type_hints["value_selection_strategy"])
        self._values: typing.Dict[str, typing.Any] = {
            "enumeration_value": enumeration_value,
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
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if value_selection_strategy is not None:
            self._values["value_selection_strategy"] = value_selection_strategy

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
    def enumeration_value(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexSlotTypeEnumerationValue"]]:
        '''enumeration_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#enumeration_value LexSlotType#enumeration_value}
        '''
        result = self._values.get("enumeration_value")
        assert result is not None, "Required property 'enumeration_value' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexSlotTypeEnumerationValue"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#name LexSlotType#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create_version LexSlotType#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#description LexSlotType#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#id LexSlotType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexSlotTypeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#timeouts LexSlotType#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexSlotTypeTimeouts"], result)

    @builtins.property
    def value_selection_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#value_selection_strategy LexSlotType#value_selection_strategy}.'''
        result = self._values.get("value_selection_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexSlotTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeEnumerationValue",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "synonyms": "synonyms"},
)
class LexSlotTypeEnumerationValue:
    def __init__(
        self,
        *,
        value: builtins.str,
        synonyms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#value LexSlotType#value}.
        :param synonyms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#synonyms LexSlotType#synonyms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotTypeEnumerationValue.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument synonyms", value=synonyms, expected_type=type_hints["synonyms"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if synonyms is not None:
            self._values["synonyms"] = synonyms

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#value LexSlotType#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def synonyms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#synonyms LexSlotType#synonyms}.'''
        result = self._values.get("synonyms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexSlotTypeEnumerationValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexSlotTypeEnumerationValueList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeEnumerationValueList",
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
            type_hints = typing.get_type_hints(LexSlotTypeEnumerationValueList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LexSlotTypeEnumerationValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotTypeEnumerationValueList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexSlotTypeEnumerationValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexSlotTypeEnumerationValue]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexSlotTypeEnumerationValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexSlotTypeEnumerationValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexSlotTypeEnumerationValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeEnumerationValueOutputReference",
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
            type_hints = typing.get_type_hints(LexSlotTypeEnumerationValueOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSynonyms")
    def reset_synonyms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSynonyms", []))

    @builtins.property
    @jsii.member(jsii_name="synonymsInput")
    def synonyms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "synonymsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="synonyms")
    def synonyms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "synonyms"))

    @synonyms.setter
    def synonyms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueOutputReference, "synonyms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synonyms", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexSlotTypeEnumerationValue, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexSlotTypeEnumerationValue, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexSlotTypeEnumerationValue, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeEnumerationValueOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexSlotTypeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create LexSlotType#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#delete LexSlotType#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#update LexSlotType#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LexSlotTypeTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#create LexSlotType#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#delete LexSlotType#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_slot_type#update LexSlotType#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexSlotTypeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexSlotTypeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lex.LexSlotTypeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LexSlotTypeTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexSlotTypeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexSlotTypeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexSlotTypeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LexSlotTypeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsLexBot",
    "DataAwsLexBotAlias",
    "DataAwsLexBotAliasConfig",
    "DataAwsLexBotConfig",
    "DataAwsLexIntent",
    "DataAwsLexIntentConfig",
    "DataAwsLexSlotType",
    "DataAwsLexSlotTypeConfig",
    "DataAwsLexSlotTypeEnumerationValue",
    "DataAwsLexSlotTypeEnumerationValueList",
    "DataAwsLexSlotTypeEnumerationValueOutputReference",
    "LexBot",
    "LexBotAbortStatement",
    "LexBotAbortStatementMessage",
    "LexBotAbortStatementMessageList",
    "LexBotAbortStatementMessageOutputReference",
    "LexBotAbortStatementOutputReference",
    "LexBotAlias",
    "LexBotAliasConfig",
    "LexBotAliasConversationLogs",
    "LexBotAliasConversationLogsLogSettings",
    "LexBotAliasConversationLogsLogSettingsList",
    "LexBotAliasConversationLogsLogSettingsOutputReference",
    "LexBotAliasConversationLogsOutputReference",
    "LexBotAliasTimeouts",
    "LexBotAliasTimeoutsOutputReference",
    "LexBotClarificationPrompt",
    "LexBotClarificationPromptMessage",
    "LexBotClarificationPromptMessageList",
    "LexBotClarificationPromptMessageOutputReference",
    "LexBotClarificationPromptOutputReference",
    "LexBotConfig",
    "LexBotIntent",
    "LexBotIntentList",
    "LexBotIntentOutputReference",
    "LexBotTimeouts",
    "LexBotTimeoutsOutputReference",
    "LexIntent",
    "LexIntentConclusionStatement",
    "LexIntentConclusionStatementMessage",
    "LexIntentConclusionStatementMessageList",
    "LexIntentConclusionStatementMessageOutputReference",
    "LexIntentConclusionStatementOutputReference",
    "LexIntentConfig",
    "LexIntentConfirmationPrompt",
    "LexIntentConfirmationPromptMessage",
    "LexIntentConfirmationPromptMessageList",
    "LexIntentConfirmationPromptMessageOutputReference",
    "LexIntentConfirmationPromptOutputReference",
    "LexIntentDialogCodeHook",
    "LexIntentDialogCodeHookOutputReference",
    "LexIntentFollowUpPrompt",
    "LexIntentFollowUpPromptOutputReference",
    "LexIntentFollowUpPromptPrompt",
    "LexIntentFollowUpPromptPromptMessage",
    "LexIntentFollowUpPromptPromptMessageList",
    "LexIntentFollowUpPromptPromptMessageOutputReference",
    "LexIntentFollowUpPromptPromptOutputReference",
    "LexIntentFollowUpPromptRejectionStatement",
    "LexIntentFollowUpPromptRejectionStatementMessage",
    "LexIntentFollowUpPromptRejectionStatementMessageList",
    "LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
    "LexIntentFollowUpPromptRejectionStatementOutputReference",
    "LexIntentFulfillmentActivity",
    "LexIntentFulfillmentActivityCodeHook",
    "LexIntentFulfillmentActivityCodeHookOutputReference",
    "LexIntentFulfillmentActivityOutputReference",
    "LexIntentRejectionStatement",
    "LexIntentRejectionStatementMessage",
    "LexIntentRejectionStatementMessageList",
    "LexIntentRejectionStatementMessageOutputReference",
    "LexIntentRejectionStatementOutputReference",
    "LexIntentSlot",
    "LexIntentSlotList",
    "LexIntentSlotOutputReference",
    "LexIntentSlotValueElicitationPrompt",
    "LexIntentSlotValueElicitationPromptMessage",
    "LexIntentSlotValueElicitationPromptMessageList",
    "LexIntentSlotValueElicitationPromptMessageOutputReference",
    "LexIntentSlotValueElicitationPromptOutputReference",
    "LexIntentTimeouts",
    "LexIntentTimeoutsOutputReference",
    "LexSlotType",
    "LexSlotTypeConfig",
    "LexSlotTypeEnumerationValue",
    "LexSlotTypeEnumerationValueList",
    "LexSlotTypeEnumerationValueOutputReference",
    "LexSlotTypeTimeouts",
    "LexSlotTypeTimeoutsOutputReference",
]

publication.publish()
