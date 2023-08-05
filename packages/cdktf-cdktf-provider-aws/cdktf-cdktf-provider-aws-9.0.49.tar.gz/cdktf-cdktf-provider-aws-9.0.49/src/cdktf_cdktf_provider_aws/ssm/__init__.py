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


class DataAwsSsmDocument(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmDocument",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_document aws_ssm_document}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        document_format: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_document aws_ssm_document} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#name DataAwsSsmDocument#name}.
        :param document_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_format DataAwsSsmDocument#document_format}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_version DataAwsSsmDocument#document_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#id DataAwsSsmDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmDocument.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmDocumentConfig(
            name=name,
            document_format=document_format,
            document_version=document_version,
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

    @jsii.member(jsii_name="resetDocumentFormat")
    def reset_document_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentFormat", []))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @builtins.property
    @jsii.member(jsii_name="documentFormatInput")
    def document_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="documentFormat")
    def document_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentFormat"))

    @document_format.setter
    def document_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmDocument, "document_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentFormat", value)

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmDocument, "document_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmDocument, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmDocument, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmDocumentConfig",
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
        "document_format": "documentFormat",
        "document_version": "documentVersion",
        "id": "id",
    },
)
class DataAwsSsmDocumentConfig(cdktf.TerraformMetaArguments):
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
        document_format: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#name DataAwsSsmDocument#name}.
        :param document_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_format DataAwsSsmDocument#document_format}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_version DataAwsSsmDocument#document_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#id DataAwsSsmDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmDocumentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument document_format", value=document_format, expected_type=type_hints["document_format"])
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
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
        if document_format is not None:
            self._values["document_format"] = document_format
        if document_version is not None:
            self._values["document_version"] = document_version
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#name DataAwsSsmDocument#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_format DataAwsSsmDocument#document_format}.'''
        result = self._values.get("document_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#document_version DataAwsSsmDocument#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_document#id DataAwsSsmDocument#id}.

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
        return "DataAwsSsmDocumentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmInstances(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmInstances",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances aws_ssm_instances}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmInstancesFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances aws_ssm_instances} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#filter DataAwsSsmInstances#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#id DataAwsSsmInstances#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmInstances.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmInstancesConfig(
            filter=filter,
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

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmInstancesFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmInstances.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsSsmInstancesFilterList":
        return typing.cast("DataAwsSsmInstancesFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="ids")
    def ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ids"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmInstancesFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmInstancesFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstances, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmInstancesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "id": "id",
    },
)
class DataAwsSsmInstancesConfig(cdktf.TerraformMetaArguments):
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
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmInstancesFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#filter DataAwsSsmInstances#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#id DataAwsSsmInstances#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmInstancesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if filter is not None:
            self._values["filter"] = filter
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
    def filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmInstancesFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#filter DataAwsSsmInstances#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmInstancesFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#id DataAwsSsmInstances#id}.

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
        return "DataAwsSsmInstancesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmInstancesFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DataAwsSsmInstancesFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#name DataAwsSsmInstances#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#values DataAwsSsmInstances#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmInstancesFilter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#name DataAwsSsmInstances#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_instances#values DataAwsSsmInstances#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmInstancesFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmInstancesFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmInstancesFilterList",
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
            type_hints = typing.get_type_hints(DataAwsSsmInstancesFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsSsmInstancesFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmInstancesFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmInstancesFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmInstancesFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmInstancesFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmInstancesFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsSsmInstancesFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmInstancesFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmInstancesFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsSsmInstancesFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsSsmInstancesFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsSsmInstancesFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmInstancesFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsSsmMaintenanceWindows(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmMaintenanceWindows",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows aws_ssm_maintenance_windows}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmMaintenanceWindowsFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows aws_ssm_maintenance_windows} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#filter DataAwsSsmMaintenanceWindows#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#id DataAwsSsmMaintenanceWindows#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindows.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmMaintenanceWindowsConfig(
            filter=filter,
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

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmMaintenanceWindowsFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindows.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsSsmMaintenanceWindowsFilterList":
        return typing.cast("DataAwsSsmMaintenanceWindowsFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="ids")
    def ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ids"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmMaintenanceWindowsFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmMaintenanceWindowsFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindows, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmMaintenanceWindowsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter": "filter",
        "id": "id",
    },
)
class DataAwsSsmMaintenanceWindowsConfig(cdktf.TerraformMetaArguments):
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
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsSsmMaintenanceWindowsFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#filter DataAwsSsmMaintenanceWindows#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#id DataAwsSsmMaintenanceWindows#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindowsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if filter is not None:
            self._values["filter"] = filter
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
    def filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmMaintenanceWindowsFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#filter DataAwsSsmMaintenanceWindows#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsSsmMaintenanceWindowsFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#id DataAwsSsmMaintenanceWindows#id}.

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
        return "DataAwsSsmMaintenanceWindowsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmMaintenanceWindowsFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DataAwsSsmMaintenanceWindowsFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#name DataAwsSsmMaintenanceWindows#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#values DataAwsSsmMaintenanceWindows#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindowsFilter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#name DataAwsSsmMaintenanceWindows#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_maintenance_windows#values DataAwsSsmMaintenanceWindows#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmMaintenanceWindowsFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmMaintenanceWindowsFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmMaintenanceWindowsFilterList",
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
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindowsFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsSsmMaintenanceWindowsFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindowsFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmMaintenanceWindowsFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmMaintenanceWindowsFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmMaintenanceWindowsFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsSsmMaintenanceWindowsFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsSsmMaintenanceWindowsFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmMaintenanceWindowsFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmMaintenanceWindowsFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsSsmMaintenanceWindowsFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsSsmMaintenanceWindowsFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsSsmMaintenanceWindowsFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmMaintenanceWindowsFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsSsmParameter(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmParameter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter aws_ssm_parameter}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        with_decryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter aws_ssm_parameter} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#name DataAwsSsmParameter#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#id DataAwsSsmParameter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param with_decryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#with_decryption DataAwsSsmParameter#with_decryption}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmParameter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmParameterConfig(
            name=name,
            id=id,
            with_decryption=with_decryption,
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

    @jsii.member(jsii_name="resetWithDecryption")
    def reset_with_decryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithDecryption", []))

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="withDecryptionInput")
    def with_decryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withDecryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParameter, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParameter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="withDecryption")
    def with_decryption(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withDecryption"))

    @with_decryption.setter
    def with_decryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParameter, "with_decryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withDecryption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmParameterConfig",
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
        "with_decryption": "withDecryption",
    },
)
class DataAwsSsmParameterConfig(cdktf.TerraformMetaArguments):
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
        with_decryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#name DataAwsSsmParameter#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#id DataAwsSsmParameter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param with_decryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#with_decryption DataAwsSsmParameter#with_decryption}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmParameterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument with_decryption", value=with_decryption, expected_type=type_hints["with_decryption"])
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
        if with_decryption is not None:
            self._values["with_decryption"] = with_decryption

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#name DataAwsSsmParameter#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#id DataAwsSsmParameter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def with_decryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameter#with_decryption DataAwsSsmParameter#with_decryption}.'''
        result = self._values.get("with_decryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmParameterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmParametersByPath(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmParametersByPath",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path aws_ssm_parameters_by_path}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        path: builtins.str,
        id: typing.Optional[builtins.str] = None,
        recursive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        with_decryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path aws_ssm_parameters_by_path} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#path DataAwsSsmParametersByPath#path}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#id DataAwsSsmParametersByPath#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param recursive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#recursive DataAwsSsmParametersByPath#recursive}.
        :param with_decryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#with_decryption DataAwsSsmParametersByPath#with_decryption}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmParametersByPath.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmParametersByPathConfig(
            path=path,
            id=id,
            recursive=recursive,
            with_decryption=with_decryption,
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

    @jsii.member(jsii_name="resetRecursive")
    def reset_recursive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecursive", []))

    @jsii.member(jsii_name="resetWithDecryption")
    def reset_with_decryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithDecryption", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arns")
    def arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arns"))

    @builtins.property
    @jsii.member(jsii_name="names")
    def names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "names"))

    @builtins.property
    @jsii.member(jsii_name="types")
    def types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "types"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="recursiveInput")
    def recursive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "recursiveInput"))

    @builtins.property
    @jsii.member(jsii_name="withDecryptionInput")
    def with_decryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withDecryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParametersByPath, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParametersByPath, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="recursive")
    def recursive(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "recursive"))

    @recursive.setter
    def recursive(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParametersByPath, "recursive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recursive", value)

    @builtins.property
    @jsii.member(jsii_name="withDecryption")
    def with_decryption(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withDecryption"))

    @with_decryption.setter
    def with_decryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmParametersByPath, "with_decryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withDecryption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmParametersByPathConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "path": "path",
        "id": "id",
        "recursive": "recursive",
        "with_decryption": "withDecryption",
    },
)
class DataAwsSsmParametersByPathConfig(cdktf.TerraformMetaArguments):
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
        path: builtins.str,
        id: typing.Optional[builtins.str] = None,
        recursive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        with_decryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#path DataAwsSsmParametersByPath#path}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#id DataAwsSsmParametersByPath#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param recursive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#recursive DataAwsSsmParametersByPath#recursive}.
        :param with_decryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#with_decryption DataAwsSsmParametersByPath#with_decryption}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmParametersByPathConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument recursive", value=recursive, expected_type=type_hints["recursive"])
            check_type(argname="argument with_decryption", value=with_decryption, expected_type=type_hints["with_decryption"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
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
        if recursive is not None:
            self._values["recursive"] = recursive
        if with_decryption is not None:
            self._values["with_decryption"] = with_decryption

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
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#path DataAwsSsmParametersByPath#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#id DataAwsSsmParametersByPath#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recursive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#recursive DataAwsSsmParametersByPath#recursive}.'''
        result = self._values.get("recursive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def with_decryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_parameters_by_path#with_decryption DataAwsSsmParametersByPath#with_decryption}.'''
        result = self._values.get("with_decryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmParametersByPathConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmPatchBaseline(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaseline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline aws_ssm_patch_baseline}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        owner: builtins.str,
        default_baseline: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline aws_ssm_patch_baseline} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#owner DataAwsSsmPatchBaseline#owner}.
        :param default_baseline: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#default_baseline DataAwsSsmPatchBaseline#default_baseline}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#id DataAwsSsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#name_prefix DataAwsSsmPatchBaseline#name_prefix}.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#operating_system DataAwsSsmPatchBaseline#operating_system}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaseline.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsSsmPatchBaselineConfig(
            owner=owner,
            default_baseline=default_baseline,
            id=id,
            name_prefix=name_prefix,
            operating_system=operating_system,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultBaseline")
    def reset_default_baseline(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBaseline", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetOperatingSystem")
    def reset_operating_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystem", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="approvalRule")
    def approval_rule(self) -> "DataAwsSsmPatchBaselineApprovalRuleList":
        return typing.cast("DataAwsSsmPatchBaselineApprovalRuleList", jsii.get(self, "approvalRule"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "approvedPatches"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approvedPatchesComplianceLevel"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="globalFilter")
    def global_filter(self) -> "DataAwsSsmPatchBaselineGlobalFilterList":
        return typing.cast("DataAwsSsmPatchBaselineGlobalFilterList", jsii.get(self, "globalFilter"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rejectedPatches"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rejectedPatchesAction"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "DataAwsSsmPatchBaselineSourceList":
        return typing.cast("DataAwsSsmPatchBaselineSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="defaultBaselineInput")
    def default_baseline_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultBaselineInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemInput")
    def operating_system_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBaseline")
    def default_baseline(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultBaseline"))

    @default_baseline.setter
    def default_baseline(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaseline, "default_baseline").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBaseline", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaseline, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaseline, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaseline, "operating_system").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaseline, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSsmPatchBaselineApprovalRule:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmPatchBaselineApprovalRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmPatchBaselineApprovalRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRuleList",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsSsmPatchBaselineApprovalRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmPatchBaselineApprovalRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsSsmPatchBaselineApprovalRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRuleOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="approveAfterDays")
    def approve_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approveAfterDays"))

    @builtins.property
    @jsii.member(jsii_name="approveUntilDate")
    def approve_until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approveUntilDate"))

    @builtins.property
    @jsii.member(jsii_name="complianceLevel")
    def compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceLevel"))

    @builtins.property
    @jsii.member(jsii_name="enableNonSecurity")
    def enable_non_security(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableNonSecurity"))

    @builtins.property
    @jsii.member(jsii_name="patchFilter")
    def patch_filter(self) -> "DataAwsSsmPatchBaselineApprovalRulePatchFilterList":
        return typing.cast("DataAwsSsmPatchBaselineApprovalRulePatchFilterList", jsii.get(self, "patchFilter"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsSsmPatchBaselineApprovalRule]:
        return typing.cast(typing.Optional[DataAwsSsmPatchBaselineApprovalRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSsmPatchBaselineApprovalRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRulePatchFilter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSsmPatchBaselineApprovalRulePatchFilter:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmPatchBaselineApprovalRulePatchFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmPatchBaselineApprovalRulePatchFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRulePatchFilterList",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRulePatchFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRulePatchFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRulePatchFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRulePatchFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRulePatchFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsSsmPatchBaselineApprovalRulePatchFilter]:
        return typing.cast(typing.Optional[DataAwsSsmPatchBaselineApprovalRulePatchFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSsmPatchBaselineApprovalRulePatchFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "owner": "owner",
        "default_baseline": "defaultBaseline",
        "id": "id",
        "name_prefix": "namePrefix",
        "operating_system": "operatingSystem",
    },
)
class DataAwsSsmPatchBaselineConfig(cdktf.TerraformMetaArguments):
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
        owner: builtins.str,
        default_baseline: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#owner DataAwsSsmPatchBaseline#owner}.
        :param default_baseline: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#default_baseline DataAwsSsmPatchBaseline#default_baseline}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#id DataAwsSsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#name_prefix DataAwsSsmPatchBaseline#name_prefix}.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#operating_system DataAwsSsmPatchBaseline#operating_system}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument default_baseline", value=default_baseline, expected_type=type_hints["default_baseline"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
        self._values: typing.Dict[str, typing.Any] = {
            "owner": owner,
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
        if default_baseline is not None:
            self._values["default_baseline"] = default_baseline
        if id is not None:
            self._values["id"] = id
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if operating_system is not None:
            self._values["operating_system"] = operating_system

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
    def owner(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#owner DataAwsSsmPatchBaseline#owner}.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_baseline(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#default_baseline DataAwsSsmPatchBaseline#default_baseline}.'''
        result = self._values.get("default_baseline")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#id DataAwsSsmPatchBaseline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#name_prefix DataAwsSsmPatchBaseline#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ssm_patch_baseline#operating_system DataAwsSsmPatchBaseline#operating_system}.'''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmPatchBaselineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineGlobalFilter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSsmPatchBaselineGlobalFilter:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmPatchBaselineGlobalFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmPatchBaselineGlobalFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineGlobalFilterList",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineGlobalFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsSsmPatchBaselineGlobalFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineGlobalFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmPatchBaselineGlobalFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineGlobalFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineGlobalFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineGlobalFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsSsmPatchBaselineGlobalFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineGlobalFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineGlobalFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsSsmPatchBaselineGlobalFilter]:
        return typing.cast(typing.Optional[DataAwsSsmPatchBaselineGlobalFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSsmPatchBaselineGlobalFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineGlobalFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineSource",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsSsmPatchBaselineSource:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsSsmPatchBaselineSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsSsmPatchBaselineSourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineSourceList",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineSourceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsSsmPatchBaselineSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineSourceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsSsmPatchBaselineSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineSourceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineSourceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineSourceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsSsmPatchBaselineSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.DataAwsSsmPatchBaselineSourceOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsSsmPatchBaselineSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="products")
    def products(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "products"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsSsmPatchBaselineSource]:
        return typing.cast(typing.Optional[DataAwsSsmPatchBaselineSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsSsmPatchBaselineSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsSsmPatchBaselineSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmActivation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmActivation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation aws_ssm_activation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        iam_role: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expiration_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        registration_limit: typing.Optional[jsii.Number] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation aws_ssm_activation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#iam_role SsmActivation#iam_role}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#description SsmActivation#description}.
        :param expiration_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#expiration_date SsmActivation#expiration_date}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#id SsmActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#name SsmActivation#name}.
        :param registration_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#registration_limit SsmActivation#registration_limit}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags SsmActivation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags_all SsmActivation#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmActivation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmActivationConfig(
            iam_role=iam_role,
            description=description,
            expiration_date=expiration_date,
            id=id,
            name=name,
            registration_limit=registration_limit,
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

    @jsii.member(jsii_name="resetExpirationDate")
    def reset_expiration_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationDate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetRegistrationLimit")
    def reset_registration_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationLimit", []))

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
    @jsii.member(jsii_name="activationCode")
    def activation_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationCode"))

    @builtins.property
    @jsii.member(jsii_name="expired")
    def expired(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "expired"))

    @builtins.property
    @jsii.member(jsii_name="registrationCount")
    def registration_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "registrationCount"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationDateInput")
    def expiration_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationDateInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleInput")
    def iam_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="registrationLimitInput")
    def registration_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "registrationLimitInput"))

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
            type_hints = typing.get_type_hints(getattr(SsmActivation, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expirationDate")
    def expiration_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationDate"))

    @expiration_date.setter
    def expiration_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "expiration_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationDate", value)

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "iam_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="registrationLimit")
    def registration_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "registrationLimit"))

    @registration_limit.setter
    def registration_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "registration_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationLimit", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmActivation, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmActivationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "iam_role": "iamRole",
        "description": "description",
        "expiration_date": "expirationDate",
        "id": "id",
        "name": "name",
        "registration_limit": "registrationLimit",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SsmActivationConfig(cdktf.TerraformMetaArguments):
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
        iam_role: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expiration_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        registration_limit: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#iam_role SsmActivation#iam_role}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#description SsmActivation#description}.
        :param expiration_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#expiration_date SsmActivation#expiration_date}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#id SsmActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#name SsmActivation#name}.
        :param registration_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#registration_limit SsmActivation#registration_limit}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags SsmActivation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags_all SsmActivation#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmActivationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expiration_date", value=expiration_date, expected_type=type_hints["expiration_date"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument registration_limit", value=registration_limit, expected_type=type_hints["registration_limit"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "iam_role": iam_role,
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
        if expiration_date is not None:
            self._values["expiration_date"] = expiration_date
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if registration_limit is not None:
            self._values["registration_limit"] = registration_limit
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
    def iam_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#iam_role SsmActivation#iam_role}.'''
        result = self._values.get("iam_role")
        assert result is not None, "Required property 'iam_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#description SsmActivation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#expiration_date SsmActivation#expiration_date}.'''
        result = self._values.get("expiration_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#id SsmActivation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#name SsmActivation#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registration_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#registration_limit SsmActivation#registration_limit}.'''
        result = self._values.get("registration_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags SsmActivation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_activation#tags_all SsmActivation#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmActivationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_association aws_ssm_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union["SsmAssociationOutputLocation", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmAssociationTargets", typing.Dict[str, typing.Any]]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_association aws_ssm_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#name SsmAssociation#name}.
        :param apply_only_at_cron_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#apply_only_at_cron_interval SsmAssociation#apply_only_at_cron_interval}.
        :param association_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#association_name SsmAssociation#association_name}.
        :param automation_target_parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#automation_target_parameter_name SsmAssociation#automation_target_parameter_name}.
        :param compliance_severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#compliance_severity SsmAssociation#compliance_severity}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#document_version SsmAssociation#document_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#id SsmAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#instance_id SsmAssociation#instance_id}.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_concurrency SsmAssociation#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_errors SsmAssociation#max_errors}.
        :param output_location: output_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#output_location SsmAssociation#output_location}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#parameters SsmAssociation#parameters}.
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#schedule_expression SsmAssociation#schedule_expression}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#targets SsmAssociation#targets}
        :param wait_for_success_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#wait_for_success_timeout_seconds SsmAssociation#wait_for_success_timeout_seconds}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmAssociationConfig(
            name=name,
            apply_only_at_cron_interval=apply_only_at_cron_interval,
            association_name=association_name,
            automation_target_parameter_name=automation_target_parameter_name,
            compliance_severity=compliance_severity,
            document_version=document_version,
            id=id,
            instance_id=instance_id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            output_location=output_location,
            parameters=parameters,
            schedule_expression=schedule_expression,
            targets=targets,
            wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putOutputLocation")
    def put_output_location(
        self,
        *,
        s3_bucket_name: builtins.str,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_bucket_name SsmAssociation#s3_bucket_name}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_key_prefix SsmAssociation#s3_key_prefix}.
        :param s3_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_region SsmAssociation#s3_region}.
        '''
        value = SsmAssociationOutputLocation(
            s3_bucket_name=s3_bucket_name,
            s3_key_prefix=s3_key_prefix,
            s3_region=s3_region,
        )

        return typing.cast(None, jsii.invoke(self, "putOutputLocation", [value]))

    @jsii.member(jsii_name="putTargets")
    def put_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmAssociationTargets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociation.put_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargets", [value]))

    @jsii.member(jsii_name="resetApplyOnlyAtCronInterval")
    def reset_apply_only_at_cron_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyOnlyAtCronInterval", []))

    @jsii.member(jsii_name="resetAssociationName")
    def reset_association_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociationName", []))

    @jsii.member(jsii_name="resetAutomationTargetParameterName")
    def reset_automation_target_parameter_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationTargetParameterName", []))

    @jsii.member(jsii_name="resetComplianceSeverity")
    def reset_compliance_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceSeverity", []))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetMaxConcurrency")
    def reset_max_concurrency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrency", []))

    @jsii.member(jsii_name="resetMaxErrors")
    def reset_max_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxErrors", []))

    @jsii.member(jsii_name="resetOutputLocation")
    def reset_output_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputLocation", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetScheduleExpression")
    def reset_schedule_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleExpression", []))

    @jsii.member(jsii_name="resetTargets")
    def reset_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargets", []))

    @jsii.member(jsii_name="resetWaitForSuccessTimeoutSeconds")
    def reset_wait_for_success_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForSuccessTimeoutSeconds", []))

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
    @jsii.member(jsii_name="associationId")
    def association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associationId"))

    @builtins.property
    @jsii.member(jsii_name="outputLocation")
    def output_location(self) -> "SsmAssociationOutputLocationOutputReference":
        return typing.cast("SsmAssociationOutputLocationOutputReference", jsii.get(self, "outputLocation"))

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> "SsmAssociationTargetsList":
        return typing.cast("SsmAssociationTargetsList", jsii.get(self, "targets"))

    @builtins.property
    @jsii.member(jsii_name="applyOnlyAtCronIntervalInput")
    def apply_only_at_cron_interval_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyOnlyAtCronIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="associationNameInput")
    def association_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="automationTargetParameterNameInput")
    def automation_target_parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationTargetParameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceSeverityInput")
    def compliance_severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceSeverityInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxErrorsInput")
    def max_errors_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputLocationInput")
    def output_location_input(self) -> typing.Optional["SsmAssociationOutputLocation"]:
        return typing.cast(typing.Optional["SsmAssociationOutputLocation"], jsii.get(self, "outputLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionInput")
    def schedule_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmAssociationTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmAssociationTargets"]]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForSuccessTimeoutSecondsInput")
    def wait_for_success_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForSuccessTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applyOnlyAtCronInterval"))

    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "apply_only_at_cron_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOnlyAtCronInterval", value)

    @builtins.property
    @jsii.member(jsii_name="associationName")
    def association_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associationName"))

    @association_name.setter
    def association_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "association_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationName", value)

    @builtins.property
    @jsii.member(jsii_name="automationTargetParameterName")
    def automation_target_parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automationTargetParameterName"))

    @automation_target_parameter_name.setter
    def automation_target_parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "automation_target_parameter_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automationTargetParameterName", value)

    @builtins.property
    @jsii.member(jsii_name="complianceSeverity")
    def compliance_severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceSeverity"))

    @compliance_severity.setter
    def compliance_severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "compliance_severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceSeverity", value)

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "document_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "max_concurrency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "max_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxErrors", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "schedule_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitForSuccessTimeoutSeconds"))

    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociation, "wait_for_success_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSuccessTimeoutSeconds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationConfig",
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
        "apply_only_at_cron_interval": "applyOnlyAtCronInterval",
        "association_name": "associationName",
        "automation_target_parameter_name": "automationTargetParameterName",
        "compliance_severity": "complianceSeverity",
        "document_version": "documentVersion",
        "id": "id",
        "instance_id": "instanceId",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "output_location": "outputLocation",
        "parameters": "parameters",
        "schedule_expression": "scheduleExpression",
        "targets": "targets",
        "wait_for_success_timeout_seconds": "waitForSuccessTimeoutSeconds",
    },
)
class SsmAssociationConfig(cdktf.TerraformMetaArguments):
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
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union["SsmAssociationOutputLocation", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmAssociationTargets", typing.Dict[str, typing.Any]]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#name SsmAssociation#name}.
        :param apply_only_at_cron_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#apply_only_at_cron_interval SsmAssociation#apply_only_at_cron_interval}.
        :param association_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#association_name SsmAssociation#association_name}.
        :param automation_target_parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#automation_target_parameter_name SsmAssociation#automation_target_parameter_name}.
        :param compliance_severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#compliance_severity SsmAssociation#compliance_severity}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#document_version SsmAssociation#document_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#id SsmAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#instance_id SsmAssociation#instance_id}.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_concurrency SsmAssociation#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_errors SsmAssociation#max_errors}.
        :param output_location: output_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#output_location SsmAssociation#output_location}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#parameters SsmAssociation#parameters}.
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#schedule_expression SsmAssociation#schedule_expression}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#targets SsmAssociation#targets}
        :param wait_for_success_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#wait_for_success_timeout_seconds SsmAssociation#wait_for_success_timeout_seconds}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(output_location, dict):
            output_location = SsmAssociationOutputLocation(**output_location)
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument apply_only_at_cron_interval", value=apply_only_at_cron_interval, expected_type=type_hints["apply_only_at_cron_interval"])
            check_type(argname="argument association_name", value=association_name, expected_type=type_hints["association_name"])
            check_type(argname="argument automation_target_parameter_name", value=automation_target_parameter_name, expected_type=type_hints["automation_target_parameter_name"])
            check_type(argname="argument compliance_severity", value=compliance_severity, expected_type=type_hints["compliance_severity"])
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_errors", value=max_errors, expected_type=type_hints["max_errors"])
            check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument wait_for_success_timeout_seconds", value=wait_for_success_timeout_seconds, expected_type=type_hints["wait_for_success_timeout_seconds"])
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
        if apply_only_at_cron_interval is not None:
            self._values["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if association_name is not None:
            self._values["association_name"] = association_name
        if automation_target_parameter_name is not None:
            self._values["automation_target_parameter_name"] = automation_target_parameter_name
        if compliance_severity is not None:
            self._values["compliance_severity"] = compliance_severity
        if document_version is not None:
            self._values["document_version"] = document_version
        if id is not None:
            self._values["id"] = id
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if output_location is not None:
            self._values["output_location"] = output_location
        if parameters is not None:
            self._values["parameters"] = parameters
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if targets is not None:
            self._values["targets"] = targets
        if wait_for_success_timeout_seconds is not None:
            self._values["wait_for_success_timeout_seconds"] = wait_for_success_timeout_seconds

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#name SsmAssociation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#apply_only_at_cron_interval SsmAssociation#apply_only_at_cron_interval}.'''
        result = self._values.get("apply_only_at_cron_interval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def association_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#association_name SsmAssociation#association_name}.'''
        result = self._values.get("association_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#automation_target_parameter_name SsmAssociation#automation_target_parameter_name}.'''
        result = self._values.get("automation_target_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#compliance_severity SsmAssociation#compliance_severity}.'''
        result = self._values.get("compliance_severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#document_version SsmAssociation#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#id SsmAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#instance_id SsmAssociation#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_concurrency SsmAssociation#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#max_errors SsmAssociation#max_errors}.'''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_location(self) -> typing.Optional["SsmAssociationOutputLocation"]:
        '''output_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#output_location SsmAssociation#output_location}
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional["SsmAssociationOutputLocation"], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#parameters SsmAssociation#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#schedule_expression SsmAssociation#schedule_expression}.'''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmAssociationTargets"]]]:
        '''targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#targets SsmAssociation#targets}
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmAssociationTargets"]]], result)

    @builtins.property
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#wait_for_success_timeout_seconds SsmAssociation#wait_for_success_timeout_seconds}.'''
        result = self._values.get("wait_for_success_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationOutputLocation",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_name": "s3BucketName",
        "s3_key_prefix": "s3KeyPrefix",
        "s3_region": "s3Region",
    },
)
class SsmAssociationOutputLocation:
    def __init__(
        self,
        *,
        s3_bucket_name: builtins.str,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_bucket_name SsmAssociation#s3_bucket_name}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_key_prefix SsmAssociation#s3_key_prefix}.
        :param s3_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_region SsmAssociation#s3_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociationOutputLocation.__init__)
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument s3_region", value=s3_region, expected_type=type_hints["s3_region"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_bucket_name": s3_bucket_name,
        }
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if s3_region is not None:
            self._values["s3_region"] = s3_region

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_bucket_name SsmAssociation#s3_bucket_name}.'''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_key_prefix SsmAssociation#s3_key_prefix}.'''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#s3_region SsmAssociation#s3_region}.'''
        result = self._values.get("s3_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmAssociationOutputLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmAssociationOutputLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationOutputLocationOutputReference",
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
            type_hints = typing.get_type_hints(SsmAssociationOutputLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetS3KeyPrefix")
    def reset_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KeyPrefix", []))

    @jsii.member(jsii_name="resetS3Region")
    def reset_s3_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Region", []))

    @builtins.property
    @jsii.member(jsii_name="s3BucketNameInput")
    def s3_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefixInput")
    def s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3RegionInput")
    def s3_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3RegionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationOutputLocationOutputReference, "s3_bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationOutputLocationOutputReference, "s3_key_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="s3Region")
    def s3_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Region"))

    @s3_region.setter
    def s3_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationOutputLocationOutputReference, "s3_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SsmAssociationOutputLocation]:
        return typing.cast(typing.Optional[SsmAssociationOutputLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmAssociationOutputLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationOutputLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmAssociationTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#key SsmAssociation#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#values SsmAssociation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociationTargets.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#key SsmAssociation#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_association#values SsmAssociation#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmAssociationTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmAssociationTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationTargetsList",
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
            type_hints = typing.get_type_hints(SsmAssociationTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmAssociationTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmAssociationTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmAssociationTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmAssociationTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmAssociationTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmAssociationTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmAssociationTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmAssociationTargetsOutputReference",
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
            type_hints = typing.get_type_hints(SsmAssociationTargetsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmAssociationTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmAssociationTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmAssociationTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmAssociationTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmDocument(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmDocument",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_document aws_ssm_document}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        content: builtins.str,
        document_type: builtins.str,
        name: builtins.str,
        attachments_source: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmDocumentAttachmentsSource", typing.Dict[str, typing.Any]]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_type: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_document aws_ssm_document} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#content SsmDocument#content}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_type SsmDocument#document_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#name SsmDocument#name}.
        :param attachments_source: attachments_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#attachments_source SsmDocument#attachments_source}
        :param document_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_format SsmDocument#document_format}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#id SsmDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#permissions SsmDocument#permissions}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags SsmDocument#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags_all SsmDocument#tags_all}.
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#target_type SsmDocument#target_type}.
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#version_name SsmDocument#version_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocument.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmDocumentConfig(
            content=content,
            document_type=document_type,
            name=name,
            attachments_source=attachments_source,
            document_format=document_format,
            id=id,
            permissions=permissions,
            tags=tags,
            tags_all=tags_all,
            target_type=target_type,
            version_name=version_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAttachmentsSource")
    def put_attachments_source(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmDocumentAttachmentsSource", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocument.put_attachments_source)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttachmentsSource", [value]))

    @jsii.member(jsii_name="resetAttachmentsSource")
    def reset_attachments_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachmentsSource", []))

    @jsii.member(jsii_name="resetDocumentFormat")
    def reset_document_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentFormat", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTargetType")
    def reset_target_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetType", []))

    @jsii.member(jsii_name="resetVersionName")
    def reset_version_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionName", []))

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
    @jsii.member(jsii_name="attachmentsSource")
    def attachments_source(self) -> "SsmDocumentAttachmentsSourceList":
        return typing.cast("SsmDocumentAttachmentsSourceList", jsii.get(self, "attachmentsSource"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="defaultVersion")
    def default_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hash"))

    @builtins.property
    @jsii.member(jsii_name="hashType")
    def hash_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashType"))

    @builtins.property
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "SsmDocumentParameterList":
        return typing.cast("SsmDocumentParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="platformTypes")
    def platform_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "platformTypes"))

    @builtins.property
    @jsii.member(jsii_name="schemaVersion")
    def schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaVersion"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="attachmentsSourceInput")
    def attachments_source_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmDocumentAttachmentsSource"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmDocumentAttachmentsSource"]]], jsii.get(self, "attachmentsSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="documentFormatInput")
    def document_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="documentTypeInput")
    def document_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "permissionsInput"))

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
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNameInput")
    def version_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="documentFormat")
    def document_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentFormat"))

    @document_format.setter
    def document_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "document_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentFormat", value)

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "document_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "target_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocument, "version_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentAttachmentsSource",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values", "name": "name"},
)
class SsmDocumentAttachmentsSource:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#key SsmDocument#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#values SsmDocument#values}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#name SsmDocument#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocumentAttachmentsSource.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#key SsmDocument#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#values SsmDocument#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#name SsmDocument#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmDocumentAttachmentsSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmDocumentAttachmentsSourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentAttachmentsSourceList",
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
            type_hints = typing.get_type_hints(SsmDocumentAttachmentsSourceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmDocumentAttachmentsSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocumentAttachmentsSourceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmDocumentAttachmentsSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmDocumentAttachmentsSource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmDocumentAttachmentsSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmDocumentAttachmentsSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmDocumentAttachmentsSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentAttachmentsSourceOutputReference",
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
            type_hints = typing.get_type_hints(SsmDocumentAttachmentsSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmDocumentAttachmentsSource, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmDocumentAttachmentsSource, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmDocumentAttachmentsSource, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentAttachmentsSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "content": "content",
        "document_type": "documentType",
        "name": "name",
        "attachments_source": "attachmentsSource",
        "document_format": "documentFormat",
        "id": "id",
        "permissions": "permissions",
        "tags": "tags",
        "tags_all": "tagsAll",
        "target_type": "targetType",
        "version_name": "versionName",
    },
)
class SsmDocumentConfig(cdktf.TerraformMetaArguments):
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
        content: builtins.str,
        document_type: builtins.str,
        name: builtins.str,
        attachments_source: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SsmDocumentAttachmentsSource, typing.Dict[str, typing.Any]]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_type: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#content SsmDocument#content}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_type SsmDocument#document_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#name SsmDocument#name}.
        :param attachments_source: attachments_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#attachments_source SsmDocument#attachments_source}
        :param document_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_format SsmDocument#document_format}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#id SsmDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#permissions SsmDocument#permissions}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags SsmDocument#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags_all SsmDocument#tags_all}.
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#target_type SsmDocument#target_type}.
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#version_name SsmDocument#version_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocumentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attachments_source", value=attachments_source, expected_type=type_hints["attachments_source"])
            check_type(argname="argument document_format", value=document_format, expected_type=type_hints["document_format"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "document_type": document_type,
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
        if attachments_source is not None:
            self._values["attachments_source"] = attachments_source
        if document_format is not None:
            self._values["document_format"] = document_format
        if id is not None:
            self._values["id"] = id
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if target_type is not None:
            self._values["target_type"] = target_type
        if version_name is not None:
            self._values["version_name"] = version_name

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
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#content SsmDocument#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def document_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_type SsmDocument#document_type}.'''
        result = self._values.get("document_type")
        assert result is not None, "Required property 'document_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#name SsmDocument#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachments_source(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmDocumentAttachmentsSource]]]:
        '''attachments_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#attachments_source SsmDocument#attachments_source}
        '''
        result = self._values.get("attachments_source")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmDocumentAttachmentsSource]]], result)

    @builtins.property
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#document_format SsmDocument#document_format}.'''
        result = self._values.get("document_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#id SsmDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#permissions SsmDocument#permissions}.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags SsmDocument#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#tags_all SsmDocument#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#target_type SsmDocument#target_type}.'''
        result = self._values.get("target_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_document#version_name SsmDocument#version_name}.'''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmDocumentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentParameter",
    jsii_struct_bases=[],
    name_mapping={},
)
class SsmDocumentParameter:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmDocumentParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmDocumentParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentParameterList",
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
            type_hints = typing.get_type_hints(SsmDocumentParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmDocumentParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmDocumentParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmDocumentParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmDocumentParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmDocumentParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class SsmDocumentParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmDocumentParameterOutputReference",
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
            type_hints = typing.get_type_hints(SsmDocumentParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SsmDocumentParameter]:
        return typing.cast(typing.Optional[SsmDocumentParameter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SsmDocumentParameter]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmDocumentParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window aws_ssm_maintenance_window}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        allow_unassociated_targets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window aws_ssm_maintenance_window} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cutoff: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#cutoff SsmMaintenanceWindow#cutoff}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#duration SsmMaintenanceWindow#duration}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#name SsmMaintenanceWindow#name}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule SsmMaintenanceWindow#schedule}.
        :param allow_unassociated_targets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#allow_unassociated_targets SsmMaintenanceWindow#allow_unassociated_targets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#description SsmMaintenanceWindow#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#enabled SsmMaintenanceWindow#enabled}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#end_date SsmMaintenanceWindow#end_date}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#id SsmMaintenanceWindow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_offset SsmMaintenanceWindow#schedule_offset}.
        :param schedule_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_timezone SsmMaintenanceWindow#schedule_timezone}.
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#start_date SsmMaintenanceWindow#start_date}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags SsmMaintenanceWindow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags_all SsmMaintenanceWindow#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindow.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmMaintenanceWindowConfig(
            cutoff=cutoff,
            duration=duration,
            name=name,
            schedule=schedule,
            allow_unassociated_targets=allow_unassociated_targets,
            description=description,
            enabled=enabled,
            end_date=end_date,
            id=id,
            schedule_offset=schedule_offset,
            schedule_timezone=schedule_timezone,
            start_date=start_date,
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

    @jsii.member(jsii_name="resetAllowUnassociatedTargets")
    def reset_allow_unassociated_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowUnassociatedTargets", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEndDate")
    def reset_end_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndDate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScheduleOffset")
    def reset_schedule_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleOffset", []))

    @jsii.member(jsii_name="resetScheduleTimezone")
    def reset_schedule_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleTimezone", []))

    @jsii.member(jsii_name="resetStartDate")
    def reset_start_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartDate", []))

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
    @jsii.member(jsii_name="allowUnassociatedTargetsInput")
    def allow_unassociated_targets_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowUnassociatedTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="cutoffInput")
    def cutoff_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cutoffInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="endDateInput")
    def end_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleOffsetInput")
    def schedule_offset_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleTimezoneInput")
    def schedule_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="startDateInput")
    def start_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDateInput"))

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
    @jsii.member(jsii_name="allowUnassociatedTargets")
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowUnassociatedTargets"))

    @allow_unassociated_targets.setter
    def allow_unassociated_targets(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "allow_unassociated_targets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUnassociatedTargets", value)

    @builtins.property
    @jsii.member(jsii_name="cutoff")
    def cutoff(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cutoff"))

    @cutoff.setter
    def cutoff(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "cutoff").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cutoff", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "end_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "schedule_offset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleOffset", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleTimezone")
    def schedule_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleTimezone"))

    @schedule_timezone.setter
    def schedule_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "schedule_timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "start_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindow, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cutoff": "cutoff",
        "duration": "duration",
        "name": "name",
        "schedule": "schedule",
        "allow_unassociated_targets": "allowUnassociatedTargets",
        "description": "description",
        "enabled": "enabled",
        "end_date": "endDate",
        "id": "id",
        "schedule_offset": "scheduleOffset",
        "schedule_timezone": "scheduleTimezone",
        "start_date": "startDate",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SsmMaintenanceWindowConfig(cdktf.TerraformMetaArguments):
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
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        allow_unassociated_targets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cutoff: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#cutoff SsmMaintenanceWindow#cutoff}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#duration SsmMaintenanceWindow#duration}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#name SsmMaintenanceWindow#name}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule SsmMaintenanceWindow#schedule}.
        :param allow_unassociated_targets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#allow_unassociated_targets SsmMaintenanceWindow#allow_unassociated_targets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#description SsmMaintenanceWindow#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#enabled SsmMaintenanceWindow#enabled}.
        :param end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#end_date SsmMaintenanceWindow#end_date}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#id SsmMaintenanceWindow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_offset SsmMaintenanceWindow#schedule_offset}.
        :param schedule_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_timezone SsmMaintenanceWindow#schedule_timezone}.
        :param start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#start_date SsmMaintenanceWindow#start_date}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags SsmMaintenanceWindow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags_all SsmMaintenanceWindow#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cutoff", value=cutoff, expected_type=type_hints["cutoff"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument allow_unassociated_targets", value=allow_unassociated_targets, expected_type=type_hints["allow_unassociated_targets"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
            check_type(argname="argument schedule_timezone", value=schedule_timezone, expected_type=type_hints["schedule_timezone"])
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "cutoff": cutoff,
            "duration": duration,
            "name": name,
            "schedule": schedule,
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
        if allow_unassociated_targets is not None:
            self._values["allow_unassociated_targets"] = allow_unassociated_targets
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if end_date is not None:
            self._values["end_date"] = end_date
        if id is not None:
            self._values["id"] = id
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_timezone is not None:
            self._values["schedule_timezone"] = schedule_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
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
    def cutoff(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#cutoff SsmMaintenanceWindow#cutoff}.'''
        result = self._values.get("cutoff")
        assert result is not None, "Required property 'cutoff' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#duration SsmMaintenanceWindow#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#name SsmMaintenanceWindow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule SsmMaintenanceWindow#schedule}.'''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_unassociated_targets(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#allow_unassociated_targets SsmMaintenanceWindow#allow_unassociated_targets}.'''
        result = self._values.get("allow_unassociated_targets")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#description SsmMaintenanceWindow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#enabled SsmMaintenanceWindow#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#end_date SsmMaintenanceWindow#end_date}.'''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#id SsmMaintenanceWindow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_offset SsmMaintenanceWindow#schedule_offset}.'''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#schedule_timezone SsmMaintenanceWindow#schedule_timezone}.'''
        result = self._values.get("schedule_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#start_date SsmMaintenanceWindow#start_date}.'''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags SsmMaintenanceWindow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window#tags_all SsmMaintenanceWindow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTarget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTarget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target aws_ssm_maintenance_window_target}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        resource_type: builtins.str,
        targets: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTargetTargets", typing.Dict[str, typing.Any]]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target aws_ssm_maintenance_window_target} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#resource_type SsmMaintenanceWindowTarget#resource_type}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#targets SsmMaintenanceWindowTarget#targets}
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#window_id SsmMaintenanceWindowTarget#window_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#description SsmMaintenanceWindowTarget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#id SsmMaintenanceWindowTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#name SsmMaintenanceWindowTarget#name}.
        :param owner_information: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#owner_information SsmMaintenanceWindowTarget#owner_information}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTarget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmMaintenanceWindowTargetConfig(
            resource_type=resource_type,
            targets=targets,
            window_id=window_id,
            description=description,
            id=id,
            name=name,
            owner_information=owner_information,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTargets")
    def put_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTargetTargets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTarget.put_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargets", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOwnerInformation")
    def reset_owner_information(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnerInformation", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> "SsmMaintenanceWindowTargetTargetsList":
        return typing.cast("SsmMaintenanceWindowTargetTargetsList", jsii.get(self, "targets"))

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
    @jsii.member(jsii_name="ownerInformationInput")
    def owner_information_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInformationInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTargetTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTargetTargets"]]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowIdInput")
    def window_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowIdInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownerInformation")
    def owner_information(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerInformation"))

    @owner_information.setter
    def owner_information(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "owner_information").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerInformation", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "resource_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTarget, "window_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTargetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "resource_type": "resourceType",
        "targets": "targets",
        "window_id": "windowId",
        "description": "description",
        "id": "id",
        "name": "name",
        "owner_information": "ownerInformation",
    },
)
class SsmMaintenanceWindowTargetConfig(cdktf.TerraformMetaArguments):
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
        resource_type: builtins.str,
        targets: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTargetTargets", typing.Dict[str, typing.Any]]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#resource_type SsmMaintenanceWindowTarget#resource_type}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#targets SsmMaintenanceWindowTarget#targets}
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#window_id SsmMaintenanceWindowTarget#window_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#description SsmMaintenanceWindowTarget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#id SsmMaintenanceWindowTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#name SsmMaintenanceWindowTarget#name}.
        :param owner_information: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#owner_information SsmMaintenanceWindowTarget#owner_information}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTargetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner_information", value=owner_information, expected_type=type_hints["owner_information"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_type": resource_type,
            "targets": targets,
            "window_id": window_id,
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
        if name is not None:
            self._values["name"] = name
        if owner_information is not None:
            self._values["owner_information"] = owner_information

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
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#resource_type SsmMaintenanceWindowTarget#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTargetTargets"]]:
        '''targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#targets SsmMaintenanceWindowTarget#targets}
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTargetTargets"]], result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#window_id SsmMaintenanceWindowTarget#window_id}.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#description SsmMaintenanceWindowTarget#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#id SsmMaintenanceWindowTarget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#name SsmMaintenanceWindowTarget#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#owner_information SsmMaintenanceWindowTarget#owner_information}.'''
        result = self._values.get("owner_information")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTargetTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmMaintenanceWindowTargetTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#key SsmMaintenanceWindowTarget#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#values SsmMaintenanceWindowTarget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTargetTargets.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#key SsmMaintenanceWindowTarget#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target#values SsmMaintenanceWindowTarget#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTargetTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTargetTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTargetTargetsList",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTargetTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTargetTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTargetTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTargetTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTargetTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTargetTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTargetTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTargetTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTargetTargetsOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTargetTargetsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTargetTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTargetTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTargetTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTargetTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTask(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTask",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task aws_ssm_maintenance_window_task}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[str, typing.Any]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParameters", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task aws_ssm_maintenance_window_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param task_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.
        :param cutoff_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        :param task_invocation_parameters: task_invocation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTask.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmMaintenanceWindowTaskConfig(
            task_arn=task_arn,
            task_type=task_type,
            window_id=window_id,
            cutoff_behavior=cutoff_behavior,
            description=description,
            id=id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            name=name,
            priority=priority,
            service_role_arn=service_role_arn,
            targets=targets,
            task_invocation_parameters=task_invocation_parameters,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTargets")
    def put_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTask.put_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargets", [value]))

    @jsii.member(jsii_name="putTaskInvocationParameters")
    def put_task_invocation_parameters(
        self,
        *,
        automation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters", typing.Dict[str, typing.Any]]] = None,
        lambda_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters", typing.Dict[str, typing.Any]]] = None,
        run_command_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters", typing.Dict[str, typing.Any]]] = None,
        step_functions_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automation_parameters: automation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        :param lambda_parameters: lambda_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        :param run_command_parameters: run_command_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        :param step_functions_parameters: step_functions_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParameters(
            automation_parameters=automation_parameters,
            lambda_parameters=lambda_parameters,
            run_command_parameters=run_command_parameters,
            step_functions_parameters=step_functions_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putTaskInvocationParameters", [value]))

    @jsii.member(jsii_name="resetCutoffBehavior")
    def reset_cutoff_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCutoffBehavior", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxConcurrency")
    def reset_max_concurrency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrency", []))

    @jsii.member(jsii_name="resetMaxErrors")
    def reset_max_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxErrors", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

    @jsii.member(jsii_name="resetTargets")
    def reset_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargets", []))

    @jsii.member(jsii_name="resetTaskInvocationParameters")
    def reset_task_invocation_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskInvocationParameters", []))

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
    @jsii.member(jsii_name="targets")
    def targets(self) -> "SsmMaintenanceWindowTaskTargetsList":
        return typing.cast("SsmMaintenanceWindowTaskTargetsList", jsii.get(self, "targets"))

    @builtins.property
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference", jsii.get(self, "taskInvocationParameters"))

    @builtins.property
    @jsii.member(jsii_name="windowTaskId")
    def window_task_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowTaskId"))

    @builtins.property
    @jsii.member(jsii_name="cutoffBehaviorInput")
    def cutoff_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cutoffBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxErrorsInput")
    def max_errors_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskArnInput")
    def task_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskArnInput"))

    @builtins.property
    @jsii.member(jsii_name="taskInvocationParametersInput")
    def task_invocation_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"], jsii.get(self, "taskInvocationParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="windowIdInput")
    def window_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cutoffBehavior")
    def cutoff_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cutoffBehavior"))

    @cutoff_behavior.setter
    def cutoff_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "cutoff_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cutoffBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "max_concurrency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "max_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxErrors", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "service_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskArn"))

    @task_arn.setter
    def task_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "task_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "task_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTask, "window_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "task_arn": "taskArn",
        "task_type": "taskType",
        "window_id": "windowId",
        "cutoff_behavior": "cutoffBehavior",
        "description": "description",
        "id": "id",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "name": "name",
        "priority": "priority",
        "service_role_arn": "serviceRoleArn",
        "targets": "targets",
        "task_invocation_parameters": "taskInvocationParameters",
    },
)
class SsmMaintenanceWindowTaskConfig(cdktf.TerraformMetaArguments):
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
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[str, typing.Any]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param task_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.
        :param cutoff_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        :param task_invocation_parameters: task_invocation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(task_invocation_parameters, dict):
            task_invocation_parameters = SsmMaintenanceWindowTaskTaskInvocationParameters(**task_invocation_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument task_arn", value=task_arn, expected_type=type_hints["task_arn"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument cutoff_behavior", value=cutoff_behavior, expected_type=type_hints["cutoff_behavior"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_errors", value=max_errors, expected_type=type_hints["max_errors"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument task_invocation_parameters", value=task_invocation_parameters, expected_type=type_hints["task_invocation_parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_arn": task_arn,
            "task_type": task_type,
            "window_id": window_id,
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
        if cutoff_behavior is not None:
            self._values["cutoff_behavior"] = cutoff_behavior
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if targets is not None:
            self._values["targets"] = targets
        if task_invocation_parameters is not None:
            self._values["task_invocation_parameters"] = task_invocation_parameters

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
    def task_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.'''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.'''
        result = self._values.get("cutoff_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.'''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]]:
        '''targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]], result)

    @builtins.property
    def task_invocation_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"]:
        '''task_invocation_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        '''
        result = self._values.get("task_invocation_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmMaintenanceWindowTaskTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#key SsmMaintenanceWindowTask#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTargets.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#key SsmMaintenanceWindowTask#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTargetsList",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTargetsOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTargetsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParameters",
    jsii_struct_bases=[],
    name_mapping={
        "automation_parameters": "automationParameters",
        "lambda_parameters": "lambdaParameters",
        "run_command_parameters": "runCommandParameters",
        "step_functions_parameters": "stepFunctionsParameters",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParameters:
    def __init__(
        self,
        *,
        automation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters", typing.Dict[str, typing.Any]]] = None,
        lambda_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters", typing.Dict[str, typing.Any]]] = None,
        run_command_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters", typing.Dict[str, typing.Any]]] = None,
        step_functions_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automation_parameters: automation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        :param lambda_parameters: lambda_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        :param run_command_parameters: run_command_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        :param step_functions_parameters: step_functions_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        if isinstance(automation_parameters, dict):
            automation_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(**automation_parameters)
        if isinstance(lambda_parameters, dict):
            lambda_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(**lambda_parameters)
        if isinstance(run_command_parameters, dict):
            run_command_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(**run_command_parameters)
        if isinstance(step_functions_parameters, dict):
            step_functions_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(**step_functions_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParameters.__init__)
            check_type(argname="argument automation_parameters", value=automation_parameters, expected_type=type_hints["automation_parameters"])
            check_type(argname="argument lambda_parameters", value=lambda_parameters, expected_type=type_hints["lambda_parameters"])
            check_type(argname="argument run_command_parameters", value=run_command_parameters, expected_type=type_hints["run_command_parameters"])
            check_type(argname="argument step_functions_parameters", value=step_functions_parameters, expected_type=type_hints["step_functions_parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automation_parameters is not None:
            self._values["automation_parameters"] = automation_parameters
        if lambda_parameters is not None:
            self._values["lambda_parameters"] = lambda_parameters
        if run_command_parameters is not None:
            self._values["run_command_parameters"] = run_command_parameters
        if step_functions_parameters is not None:
            self._values["step_functions_parameters"] = step_functions_parameters

    @builtins.property
    def automation_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters"]:
        '''automation_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        '''
        result = self._values.get("automation_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters"], result)

    @builtins.property
    def lambda_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters"]:
        '''lambda_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        '''
        result = self._values.get("lambda_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters"], result)

    @builtins.property
    def run_command_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"]:
        '''run_command_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        '''
        result = self._values.get("run_command_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"], result)

    @builtins.property
    def step_functions_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"]:
        '''step_functions_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        result = self._values.get("step_functions_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters",
    jsii_struct_bases=[],
    name_mapping={"document_version": "documentVersion", "parameter": "parameter"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters:
    def __init__(
        self,
        *,
        document_version: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters.__init__)
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if document_version is not None:
            self._values["document_version"] = document_version
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference, "document_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters",
    jsii_struct_bases=[],
    name_mapping={
        "client_context": "clientContext",
        "payload": "payload",
        "qualifier": "qualifier",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters:
    def __init__(
        self,
        *,
        client_context: typing.Optional[builtins.str] = None,
        payload: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.
        :param payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters.__init__)
            check_type(argname="argument client_context", value=client_context, expected_type=type_hints["client_context"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_context is not None:
            self._values["client_context"] = client_context
        if payload is not None:
            self._values["payload"] = payload
        if qualifier is not None:
            self._values["qualifier"] = qualifier

    @builtins.property
    def client_context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.'''
        result = self._values.get("client_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.'''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.'''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientContext")
    def reset_client_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientContext", []))

    @jsii.member(jsii_name="resetPayload")
    def reset_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayload", []))

    @jsii.member(jsii_name="resetQualifier")
    def reset_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQualifier", []))

    @builtins.property
    @jsii.member(jsii_name="clientContextInput")
    def client_context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientContextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="clientContext")
    def client_context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientContext"))

    @client_context.setter
    def client_context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, "client_context").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientContext", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, "payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, "qualifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomationParameters")
    def put_automation_parameters(
        self,
        *,
        document_version: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(
            document_version=document_version, parameter=parameter
        )

        return typing.cast(None, jsii.invoke(self, "putAutomationParameters", [value]))

    @jsii.member(jsii_name="putLambdaParameters")
    def put_lambda_parameters(
        self,
        *,
        client_context: typing.Optional[builtins.str] = None,
        payload: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.
        :param payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(
            client_context=client_context, payload=payload, qualifier=qualifier
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaParameters", [value]))

    @jsii.member(jsii_name="putRunCommandParameters")
    def put_run_command_parameters(
        self,
        *,
        cloudwatch_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig", typing.Dict[str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        document_hash: typing.Optional[builtins.str] = None,
        document_hash_type: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig", typing.Dict[str, typing.Any]]] = None,
        output_s3_bucket: typing.Optional[builtins.str] = None,
        output_s3_key_prefix: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[str, typing.Any]]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cloudwatch_config: cloudwatch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.
        :param document_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.
        :param document_hash_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        :param output_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.
        :param output_s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(
            cloudwatch_config=cloudwatch_config,
            comment=comment,
            document_hash=document_hash,
            document_hash_type=document_hash_type,
            document_version=document_version,
            notification_config=notification_config,
            output_s3_bucket=output_s3_bucket,
            output_s3_key_prefix=output_s3_key_prefix,
            parameter=parameter,
            service_role_arn=service_role_arn,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putRunCommandParameters", [value]))

    @jsii.member(jsii_name="putStepFunctionsParameters")
    def put_step_functions_parameters(
        self,
        *,
        input: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(
            input=input, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putStepFunctionsParameters", [value]))

    @jsii.member(jsii_name="resetAutomationParameters")
    def reset_automation_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationParameters", []))

    @jsii.member(jsii_name="resetLambdaParameters")
    def reset_lambda_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaParameters", []))

    @jsii.member(jsii_name="resetRunCommandParameters")
    def reset_run_command_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommandParameters", []))

    @jsii.member(jsii_name="resetStepFunctionsParameters")
    def reset_step_functions_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepFunctionsParameters", []))

    @builtins.property
    @jsii.member(jsii_name="automationParameters")
    def automation_parameters(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference, jsii.get(self, "automationParameters"))

    @builtins.property
    @jsii.member(jsii_name="lambdaParameters")
    def lambda_parameters(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, jsii.get(self, "lambdaParameters"))

    @builtins.property
    @jsii.member(jsii_name="runCommandParameters")
    def run_command_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference", jsii.get(self, "runCommandParameters"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsParameters")
    def step_functions_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference", jsii.get(self, "stepFunctionsParameters"))

    @builtins.property
    @jsii.member(jsii_name="automationParametersInput")
    def automation_parameters_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters], jsii.get(self, "automationParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaParametersInput")
    def lambda_parameters_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters], jsii.get(self, "lambdaParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandParametersInput")
    def run_command_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"], jsii.get(self, "runCommandParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsParametersInput")
    def step_functions_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"], jsii.get(self, "stepFunctionsParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_config": "cloudwatchConfig",
        "comment": "comment",
        "document_hash": "documentHash",
        "document_hash_type": "documentHashType",
        "document_version": "documentVersion",
        "notification_config": "notificationConfig",
        "output_s3_bucket": "outputS3Bucket",
        "output_s3_key_prefix": "outputS3KeyPrefix",
        "parameter": "parameter",
        "service_role_arn": "serviceRoleArn",
        "timeout_seconds": "timeoutSeconds",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters:
    def __init__(
        self,
        *,
        cloudwatch_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig", typing.Dict[str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        document_hash: typing.Optional[builtins.str] = None,
        document_hash_type: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig", typing.Dict[str, typing.Any]]] = None,
        output_s3_bucket: typing.Optional[builtins.str] = None,
        output_s3_key_prefix: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[str, typing.Any]]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cloudwatch_config: cloudwatch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.
        :param document_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.
        :param document_hash_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        :param output_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.
        :param output_s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.
        '''
        if isinstance(cloudwatch_config, dict):
            cloudwatch_config = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(**cloudwatch_config)
        if isinstance(notification_config, dict):
            notification_config = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(**notification_config)
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters.__init__)
            check_type(argname="argument cloudwatch_config", value=cloudwatch_config, expected_type=type_hints["cloudwatch_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument document_hash", value=document_hash, expected_type=type_hints["document_hash"])
            check_type(argname="argument document_hash_type", value=document_hash_type, expected_type=type_hints["document_hash_type"])
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
            check_type(argname="argument output_s3_bucket", value=output_s3_bucket, expected_type=type_hints["output_s3_bucket"])
            check_type(argname="argument output_s3_key_prefix", value=output_s3_key_prefix, expected_type=type_hints["output_s3_key_prefix"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_config is not None:
            self._values["cloudwatch_config"] = cloudwatch_config
        if comment is not None:
            self._values["comment"] = comment
        if document_hash is not None:
            self._values["document_hash"] = document_hash
        if document_hash_type is not None:
            self._values["document_hash_type"] = document_hash_type
        if document_version is not None:
            self._values["document_version"] = document_version
        if notification_config is not None:
            self._values["notification_config"] = notification_config
        if output_s3_bucket is not None:
            self._values["output_s3_bucket"] = output_s3_bucket
        if output_s3_key_prefix is not None:
            self._values["output_s3_key_prefix"] = output_s3_key_prefix
        if parameter is not None:
            self._values["parameter"] = parameter
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def cloudwatch_config(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig"]:
        '''cloudwatch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        '''
        result = self._values.get("cloudwatch_config")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig"], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.'''
        result = self._values.get("document_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_hash_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.'''
        result = self._values.get("document_hash_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_config(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig"]:
        '''notification_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        '''
        result = self._values.get("notification_config")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig"], result)

    @builtins.property
    def output_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.'''
        result = self._values.get("output_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.'''
        result = self._values.get("output_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group_name": "cloudwatchLogGroupName",
        "cloudwatch_output_enabled": "cloudwatchOutputEnabled",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig:
    def __init__(
        self,
        *,
        cloudwatch_log_group_name: typing.Optional[builtins.str] = None,
        cloudwatch_output_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.
        :param cloudwatch_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig.__init__)
            check_type(argname="argument cloudwatch_log_group_name", value=cloudwatch_log_group_name, expected_type=type_hints["cloudwatch_log_group_name"])
            check_type(argname="argument cloudwatch_output_enabled", value=cloudwatch_output_enabled, expected_type=type_hints["cloudwatch_output_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_log_group_name is not None:
            self._values["cloudwatch_log_group_name"] = cloudwatch_log_group_name
        if cloudwatch_output_enabled is not None:
            self._values["cloudwatch_output_enabled"] = cloudwatch_output_enabled

    @builtins.property
    def cloudwatch_log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.'''
        result = self._values.get("cloudwatch_log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatch_output_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.'''
        result = self._values.get("cloudwatch_output_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudwatchLogGroupName")
    def reset_cloudwatch_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogGroupName", []))

    @jsii.member(jsii_name="resetCloudwatchOutputEnabled")
    def reset_cloudwatch_output_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchOutputEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupNameInput")
    def cloudwatch_log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchOutputEnabledInput")
    def cloudwatch_output_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cloudwatchOutputEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupName")
    def cloudwatch_log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupName"))

    @cloudwatch_log_group_name.setter
    def cloudwatch_log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference, "cloudwatch_log_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cloudwatchOutputEnabled")
    def cloudwatch_output_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cloudwatchOutputEnabled"))

    @cloudwatch_output_enabled.setter
    def cloudwatch_output_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference, "cloudwatch_output_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchOutputEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arn": "notificationArn",
        "notification_events": "notificationEvents",
        "notification_type": "notificationType",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig:
    def __init__(
        self,
        *,
        notification_arn: typing.Optional[builtins.str] = None,
        notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.
        :param notification_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig.__init__)
            check_type(argname="argument notification_arn", value=notification_arn, expected_type=type_hints["notification_arn"])
            check_type(argname="argument notification_events", value=notification_events, expected_type=type_hints["notification_events"])
            check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if notification_arn is not None:
            self._values["notification_arn"] = notification_arn
        if notification_events is not None:
            self._values["notification_events"] = notification_events
        if notification_type is not None:
            self._values["notification_type"] = notification_type

    @builtins.property
    def notification_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.'''
        result = self._values.get("notification_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.'''
        result = self._values.get("notification_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def notification_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.'''
        result = self._values.get("notification_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotificationArn")
    def reset_notification_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationArn", []))

    @jsii.member(jsii_name="resetNotificationEvents")
    def reset_notification_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEvents", []))

    @jsii.member(jsii_name="resetNotificationType")
    def reset_notification_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationType", []))

    @builtins.property
    @jsii.member(jsii_name="notificationArnInput")
    def notification_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEventsInput")
    def notification_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTypeInput")
    def notification_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationArn")
    def notification_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationArn"))

    @notification_arn.setter
    def notification_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, "notification_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArn", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEvents")
    def notification_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEvents"))

    @notification_events.setter
    def notification_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, "notification_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEvents", value)

    @builtins.property
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, "notification_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchConfig")
    def put_cloudwatch_config(
        self,
        *,
        cloudwatch_log_group_name: typing.Optional[builtins.str] = None,
        cloudwatch_output_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.
        :param cloudwatch_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(
            cloudwatch_log_group_name=cloudwatch_log_group_name,
            cloudwatch_output_enabled=cloudwatch_output_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfig", [value]))

    @jsii.member(jsii_name="putNotificationConfig")
    def put_notification_config(
        self,
        *,
        notification_arn: typing.Optional[builtins.str] = None,
        notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.
        :param notification_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(
            notification_arn=notification_arn,
            notification_events=notification_events,
            notification_type=notification_type,
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfig", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetCloudwatchConfig")
    def reset_cloudwatch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchConfig", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDocumentHash")
    def reset_document_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentHash", []))

    @jsii.member(jsii_name="resetDocumentHashType")
    def reset_document_hash_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentHashType", []))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

    @jsii.member(jsii_name="resetNotificationConfig")
    def reset_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfig", []))

    @jsii.member(jsii_name="resetOutputS3Bucket")
    def reset_output_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputS3Bucket", []))

    @jsii.member(jsii_name="resetOutputS3KeyPrefix")
    def reset_output_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputS3KeyPrefix", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchConfig")
    def cloudwatch_config(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference, jsii.get(self, "cloudwatchConfig"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfig")
    def notification_config(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, jsii.get(self, "notificationConfig"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchConfigInput")
    def cloudwatch_config_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig], jsii.get(self, "cloudwatchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="documentHashInput")
    def document_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentHashInput"))

    @builtins.property
    @jsii.member(jsii_name="documentHashTypeInput")
    def document_hash_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentHashTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigInput")
    def notification_config_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig], jsii.get(self, "notificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputS3BucketInput")
    def output_s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputS3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="outputS3KeyPrefixInput")
    def output_s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputS3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="documentHash")
    def document_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentHash"))

    @document_hash.setter
    def document_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "document_hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentHash", value)

    @builtins.property
    @jsii.member(jsii_name="documentHashType")
    def document_hash_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentHashType"))

    @document_hash_type.setter
    def document_hash_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "document_hash_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentHashType", value)

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "document_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="outputS3Bucket")
    def output_s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputS3Bucket"))

    @output_s3_bucket.setter
    def output_s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "output_s3_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="outputS3KeyPrefix")
    def output_s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputS3KeyPrefix"))

    @output_s3_key_prefix.setter
    def output_s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "output_s3_key_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "service_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters",
    jsii_struct_bases=[],
    name_mapping={"input": "input", "name": "name"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters:
    def __init__(
        self,
        *,
        input: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters.__init__)
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if input is not None:
            self._values["input"] = input
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def input(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.'''
        result = self._values.get("input")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference",
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
            type_hints = typing.get_type_hints(SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "input"))

    @input.setter
    def input(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference, "input").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "input", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmParameter(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmParameter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter aws_ssm_parameter}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_value: typing.Optional[builtins.str] = None,
        key_id: typing.Optional[builtins.str] = None,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter aws_ssm_parameter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#name SsmParameter#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#type SsmParameter#type}.
        :param allowed_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#allowed_pattern SsmParameter#allowed_pattern}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#arn SsmParameter#arn}.
        :param data_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#data_type SsmParameter#data_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#description SsmParameter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#id SsmParameter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#insecure_value SsmParameter#insecure_value}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#key_id SsmParameter#key_id}.
        :param overwrite: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#overwrite SsmParameter#overwrite}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags SsmParameter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags_all SsmParameter#tags_all}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tier SsmParameter#tier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#value SsmParameter#value}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmParameter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmParameterConfig(
            name=name,
            type=type,
            allowed_pattern=allowed_pattern,
            arn=arn,
            data_type=data_type,
            description=description,
            id=id,
            insecure_value=insecure_value,
            key_id=key_id,
            overwrite=overwrite,
            tags=tags,
            tags_all=tags_all,
            tier=tier,
            value=value,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowedPattern")
    def reset_allowed_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedPattern", []))

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInsecureValue")
    def reset_insecure_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureValue", []))

    @jsii.member(jsii_name="resetKeyId")
    def reset_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyId", []))

    @jsii.member(jsii_name="resetOverwrite")
    def reset_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwrite", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="allowedPatternInput")
    def allowed_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureValueInput")
    def insecure_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insecureValueInput"))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteInput")
    def overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteInput"))

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
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedPattern"))

    @allowed_pattern.setter
    def allowed_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "allowed_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPattern", value)

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "data_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="insecureValue")
    def insecure_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "insecureValue"))

    @insecure_value.setter
    def insecure_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "insecure_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureValue", value)

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overwrite")
    def overwrite(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwrite"))

    @overwrite.setter
    def overwrite(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "overwrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwrite", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmParameter, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmParameterConfig",
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
        "type": "type",
        "allowed_pattern": "allowedPattern",
        "arn": "arn",
        "data_type": "dataType",
        "description": "description",
        "id": "id",
        "insecure_value": "insecureValue",
        "key_id": "keyId",
        "overwrite": "overwrite",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tier": "tier",
        "value": "value",
    },
)
class SsmParameterConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        arn: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_value: typing.Optional[builtins.str] = None,
        key_id: typing.Optional[builtins.str] = None,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#name SsmParameter#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#type SsmParameter#type}.
        :param allowed_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#allowed_pattern SsmParameter#allowed_pattern}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#arn SsmParameter#arn}.
        :param data_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#data_type SsmParameter#data_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#description SsmParameter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#id SsmParameter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#insecure_value SsmParameter#insecure_value}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#key_id SsmParameter#key_id}.
        :param overwrite: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#overwrite SsmParameter#overwrite}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags SsmParameter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags_all SsmParameter#tags_all}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tier SsmParameter#tier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#value SsmParameter#value}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmParameterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument allowed_pattern", value=allowed_pattern, expected_type=type_hints["allowed_pattern"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insecure_value", value=insecure_value, expected_type=type_hints["insecure_value"])
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if arn is not None:
            self._values["arn"] = arn
        if data_type is not None:
            self._values["data_type"] = data_type
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if insecure_value is not None:
            self._values["insecure_value"] = insecure_value
        if key_id is not None:
            self._values["key_id"] = key_id
        if overwrite is not None:
            self._values["overwrite"] = overwrite
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tier is not None:
            self._values["tier"] = tier
        if value is not None:
            self._values["value"] = value

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#name SsmParameter#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#type SsmParameter#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#allowed_pattern SsmParameter#allowed_pattern}.'''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#arn SsmParameter#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#data_type SsmParameter#data_type}.'''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#description SsmParameter#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#id SsmParameter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#insecure_value SsmParameter#insecure_value}.'''
        result = self._values.get("insecure_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#key_id SsmParameter#key_id}.'''
        result = self._values.get("key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#overwrite SsmParameter#overwrite}.'''
        result = self._values.get("overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags SsmParameter#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tags_all SsmParameter#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#tier SsmParameter#tier}.'''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_parameter#value SsmParameter#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmParameterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaseline(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaseline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline aws_ssm_patch_baseline}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        approval_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRule", typing.Dict[str, typing.Any]]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline aws_ssm_patch_baseline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param approval_rule: approval_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        :param approved_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.
        :param approved_patches_compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.
        :param approved_patches_enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.
        :param global_filter: global_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.
        :param rejected_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.
        :param rejected_patches_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaseline.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmPatchBaselineConfig(
            name=name,
            approval_rule=approval_rule,
            approved_patches=approved_patches,
            approved_patches_compliance_level=approved_patches_compliance_level,
            approved_patches_enable_non_security=approved_patches_enable_non_security,
            description=description,
            global_filter=global_filter,
            id=id,
            operating_system=operating_system,
            rejected_patches=rejected_patches,
            rejected_patches_action=rejected_patches_action,
            source=source,
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

    @jsii.member(jsii_name="putApprovalRule")
    def put_approval_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaseline.put_approval_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApprovalRule", [value]))

    @jsii.member(jsii_name="putGlobalFilter")
    def put_global_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaseline.put_global_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGlobalFilter", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaseline.put_source)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetApprovalRule")
    def reset_approval_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalRule", []))

    @jsii.member(jsii_name="resetApprovedPatches")
    def reset_approved_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatches", []))

    @jsii.member(jsii_name="resetApprovedPatchesComplianceLevel")
    def reset_approved_patches_compliance_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatchesComplianceLevel", []))

    @jsii.member(jsii_name="resetApprovedPatchesEnableNonSecurity")
    def reset_approved_patches_enable_non_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatchesEnableNonSecurity", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGlobalFilter")
    def reset_global_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperatingSystem")
    def reset_operating_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystem", []))

    @jsii.member(jsii_name="resetRejectedPatches")
    def reset_rejected_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedPatches", []))

    @jsii.member(jsii_name="resetRejectedPatchesAction")
    def reset_rejected_patches_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedPatchesAction", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

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
    @jsii.member(jsii_name="approvalRule")
    def approval_rule(self) -> "SsmPatchBaselineApprovalRuleList":
        return typing.cast("SsmPatchBaselineApprovalRuleList", jsii.get(self, "approvalRule"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="globalFilter")
    def global_filter(self) -> "SsmPatchBaselineGlobalFilterList":
        return typing.cast("SsmPatchBaselineGlobalFilterList", jsii.get(self, "globalFilter"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "SsmPatchBaselineSourceList":
        return typing.cast("SsmPatchBaselineSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="approvalRuleInput")
    def approval_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRule"]]], jsii.get(self, "approvalRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevelInput")
    def approved_patches_compliance_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvedPatchesComplianceLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurityInput")
    def approved_patches_enable_non_security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "approvedPatchesEnableNonSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesInput")
    def approved_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "approvedPatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="globalFilterInput")
    def global_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]], jsii.get(self, "globalFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemInput")
    def operating_system_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesActionInput")
    def rejected_patches_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rejectedPatchesActionInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesInput")
    def rejected_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rejectedPatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineSource"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineSource"]]], jsii.get(self, "sourceInput"))

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
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "approvedPatches"))

    @approved_patches.setter
    def approved_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "approved_patches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approvedPatchesComplianceLevel"))

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "approved_patches_compliance_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesComplianceLevel", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "approved_patches_enable_non_security").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "operating_system").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rejectedPatches"))

    @rejected_patches.setter
    def rejected_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "rejected_patches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rejectedPatchesAction"))

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "rejected_patches_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatchesAction", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaseline, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRule",
    jsii_struct_bases=[],
    name_mapping={
        "patch_filter": "patchFilter",
        "approve_after_days": "approveAfterDays",
        "approve_until_date": "approveUntilDate",
        "compliance_level": "complianceLevel",
        "enable_non_security": "enableNonSecurity",
    },
)
class SsmPatchBaselineApprovalRule:
    def __init__(
        self,
        *,
        patch_filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRulePatchFilter", typing.Dict[str, typing.Any]]]],
        approve_after_days: typing.Optional[jsii.Number] = None,
        approve_until_date: typing.Optional[builtins.str] = None,
        compliance_level: typing.Optional[builtins.str] = None,
        enable_non_security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param patch_filter: patch_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#patch_filter SsmPatchBaseline#patch_filter}
        :param approve_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_after_days SsmPatchBaseline#approve_after_days}.
        :param approve_until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_until_date SsmPatchBaseline#approve_until_date}.
        :param compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#compliance_level SsmPatchBaseline#compliance_level}.
        :param enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#enable_non_security SsmPatchBaseline#enable_non_security}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRule.__init__)
            check_type(argname="argument patch_filter", value=patch_filter, expected_type=type_hints["patch_filter"])
            check_type(argname="argument approve_after_days", value=approve_after_days, expected_type=type_hints["approve_after_days"])
            check_type(argname="argument approve_until_date", value=approve_until_date, expected_type=type_hints["approve_until_date"])
            check_type(argname="argument compliance_level", value=compliance_level, expected_type=type_hints["compliance_level"])
            check_type(argname="argument enable_non_security", value=enable_non_security, expected_type=type_hints["enable_non_security"])
        self._values: typing.Dict[str, typing.Any] = {
            "patch_filter": patch_filter,
        }
        if approve_after_days is not None:
            self._values["approve_after_days"] = approve_after_days
        if approve_until_date is not None:
            self._values["approve_until_date"] = approve_until_date
        if compliance_level is not None:
            self._values["compliance_level"] = compliance_level
        if enable_non_security is not None:
            self._values["enable_non_security"] = enable_non_security

    @builtins.property
    def patch_filter(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]:
        '''patch_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#patch_filter SsmPatchBaseline#patch_filter}
        '''
        result = self._values.get("patch_filter")
        assert result is not None, "Required property 'patch_filter' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]], result)

    @builtins.property
    def approve_after_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_after_days SsmPatchBaseline#approve_after_days}.'''
        result = self._values.get("approve_after_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def approve_until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_until_date SsmPatchBaseline#approve_until_date}.'''
        result = self._values.get("approve_until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compliance_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#compliance_level SsmPatchBaseline#compliance_level}.'''
        result = self._values.get("compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#enable_non_security SsmPatchBaseline#enable_non_security}.'''
        result = self._values.get("enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineApprovalRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineApprovalRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRuleList",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineApprovalRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineApprovalRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineApprovalRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRuleOutputReference",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPatchFilter")
    def put_patch_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRulePatchFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRuleOutputReference.put_patch_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPatchFilter", [value]))

    @jsii.member(jsii_name="resetApproveAfterDays")
    def reset_approve_after_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApproveAfterDays", []))

    @jsii.member(jsii_name="resetApproveUntilDate")
    def reset_approve_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApproveUntilDate", []))

    @jsii.member(jsii_name="resetComplianceLevel")
    def reset_compliance_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceLevel", []))

    @jsii.member(jsii_name="resetEnableNonSecurity")
    def reset_enable_non_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNonSecurity", []))

    @builtins.property
    @jsii.member(jsii_name="patchFilter")
    def patch_filter(self) -> "SsmPatchBaselineApprovalRulePatchFilterList":
        return typing.cast("SsmPatchBaselineApprovalRulePatchFilterList", jsii.get(self, "patchFilter"))

    @builtins.property
    @jsii.member(jsii_name="approveAfterDaysInput")
    def approve_after_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "approveAfterDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="approveUntilDateInput")
    def approve_until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approveUntilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceLevelInput")
    def compliance_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNonSecurityInput")
    def enable_non_security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableNonSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="patchFilterInput")
    def patch_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]], jsii.get(self, "patchFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="approveAfterDays")
    def approve_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approveAfterDays"))

    @approve_after_days.setter
    def approve_after_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleOutputReference, "approve_after_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approveAfterDays", value)

    @builtins.property
    @jsii.member(jsii_name="approveUntilDate")
    def approve_until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approveUntilDate"))

    @approve_until_date.setter
    def approve_until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleOutputReference, "approve_until_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approveUntilDate", value)

    @builtins.property
    @jsii.member(jsii_name="complianceLevel")
    def compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceLevel"))

    @compliance_level.setter
    def compliance_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleOutputReference, "compliance_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceLevel", value)

    @builtins.property
    @jsii.member(jsii_name="enableNonSecurity")
    def enable_non_security(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableNonSecurity"))

    @enable_non_security.setter
    def enable_non_security(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleOutputReference, "enable_non_security").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNonSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRulePatchFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmPatchBaselineApprovalRulePatchFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRulePatchFilter.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineApprovalRulePatchFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineApprovalRulePatchFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRulePatchFilterList",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRulePatchFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmPatchBaselineApprovalRulePatchFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRulePatchFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineApprovalRulePatchFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineApprovalRulePatchFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineApprovalRulePatchFilterOutputReference",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineApprovalRulePatchFilterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineApprovalRulePatchFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineConfig",
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
        "approval_rule": "approvalRule",
        "approved_patches": "approvedPatches",
        "approved_patches_compliance_level": "approvedPatchesComplianceLevel",
        "approved_patches_enable_non_security": "approvedPatchesEnableNonSecurity",
        "description": "description",
        "global_filter": "globalFilter",
        "id": "id",
        "operating_system": "operatingSystem",
        "rejected_patches": "rejectedPatches",
        "rejected_patches_action": "rejectedPatchesAction",
        "source": "source",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SsmPatchBaselineConfig(cdktf.TerraformMetaArguments):
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
        approval_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRule, typing.Dict[str, typing.Any]]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param approval_rule: approval_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        :param approved_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.
        :param approved_patches_compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.
        :param approved_patches_enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.
        :param global_filter: global_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.
        :param rejected_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.
        :param rejected_patches_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument approval_rule", value=approval_rule, expected_type=type_hints["approval_rule"])
            check_type(argname="argument approved_patches", value=approved_patches, expected_type=type_hints["approved_patches"])
            check_type(argname="argument approved_patches_compliance_level", value=approved_patches_compliance_level, expected_type=type_hints["approved_patches_compliance_level"])
            check_type(argname="argument approved_patches_enable_non_security", value=approved_patches_enable_non_security, expected_type=type_hints["approved_patches_enable_non_security"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument global_filter", value=global_filter, expected_type=type_hints["global_filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument rejected_patches", value=rejected_patches, expected_type=type_hints["rejected_patches"])
            check_type(argname="argument rejected_patches_action", value=rejected_patches_action, expected_type=type_hints["rejected_patches_action"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
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
        if approval_rule is not None:
            self._values["approval_rule"] = approval_rule
        if approved_patches is not None:
            self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None:
            self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if description is not None:
            self._values["description"] = description
        if global_filter is not None:
            self._values["global_filter"] = global_filter
        if id is not None:
            self._values["id"] = id
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if rejected_patches is not None:
            self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            self._values["rejected_patches_action"] = rejected_patches_action
        if source is not None:
            self._values["source"] = source
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]]:
        '''approval_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        '''
        result = self._values.get("approval_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]], result)

    @builtins.property
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.'''
        result = self._values.get("approved_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.'''
        result = self._values.get("approved_patches_compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.'''
        result = self._values.get("approved_patches_enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]]:
        '''global_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        '''
        result = self._values.get("global_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.'''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.'''
        result = self._values.get("rejected_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.'''
        result = self._values.get("rejected_patches_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SsmPatchBaselineSource"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineGlobalFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmPatchBaselineGlobalFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineGlobalFilter.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineGlobalFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineGlobalFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineGlobalFilterList",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineGlobalFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineGlobalFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineGlobalFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineGlobalFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineGlobalFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineGlobalFilterOutputReference",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineGlobalFilterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineGlobalFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineSource",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "name": "name",
        "products": "products",
    },
)
class SsmPatchBaselineSource:
    def __init__(
        self,
        *,
        configuration: builtins.str,
        name: builtins.str,
        products: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#configuration SsmPatchBaseline#configuration}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param products: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#products SsmPatchBaseline#products}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineSource.__init__)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument products", value=products, expected_type=type_hints["products"])
        self._values: typing.Dict[str, typing.Any] = {
            "configuration": configuration,
            "name": name,
            "products": products,
        }

    @builtins.property
    def configuration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#configuration SsmPatchBaseline#configuration}.'''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def products(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#products SsmPatchBaseline#products}.'''
        result = self._values.get("products")
        assert result is not None, "Required property 'products' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineSourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineSourceList",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineSourceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchBaselineSourceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineSource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SsmPatchBaselineSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchBaselineSourceOutputReference",
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
            type_hints = typing.get_type_hints(SsmPatchBaselineSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productsInput")
    def products_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productsInput"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceOutputReference, "configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="products")
    def products(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "products"))

    @products.setter
    def products(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceOutputReference, "products").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "products", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineSource, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineSource, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineSource, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchBaselineSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group aws_ssm_patch_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        baseline_id: builtins.str,
        patch_group: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group aws_ssm_patch_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param baseline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#baseline_id SsmPatchGroup#baseline_id}.
        :param patch_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#patch_group SsmPatchGroup#patch_group}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#id SsmPatchGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmPatchGroupConfig(
            baseline_id=baseline_id,
            patch_group=patch_group,
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
    @jsii.member(jsii_name="baselineIdInput")
    def baseline_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baselineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="patchGroupInput")
    def patch_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patchGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineId")
    def baseline_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baselineId"))

    @baseline_id.setter
    def baseline_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchGroup, "baseline_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="patchGroup")
    def patch_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchGroup"))

    @patch_group.setter
    def patch_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmPatchGroup, "patch_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchGroup", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmPatchGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "baseline_id": "baselineId",
        "patch_group": "patchGroup",
        "id": "id",
    },
)
class SsmPatchGroupConfig(cdktf.TerraformMetaArguments):
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
        baseline_id: builtins.str,
        patch_group: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param baseline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#baseline_id SsmPatchGroup#baseline_id}.
        :param patch_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#patch_group SsmPatchGroup#patch_group}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#id SsmPatchGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmPatchGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument baseline_id", value=baseline_id, expected_type=type_hints["baseline_id"])
            check_type(argname="argument patch_group", value=patch_group, expected_type=type_hints["patch_group"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "baseline_id": baseline_id,
            "patch_group": patch_group,
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
    def baseline_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#baseline_id SsmPatchGroup#baseline_id}.'''
        result = self._values.get("baseline_id")
        assert result is not None, "Required property 'baseline_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def patch_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#patch_group SsmPatchGroup#patch_group}.'''
        result = self._values.get("patch_group")
        assert result is not None, "Required property 'patch_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_group#id SsmPatchGroup#id}.

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
        return "SsmPatchGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmResourceDataSync(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmResourceDataSync",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync aws_ssm_resource_data_sync}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        s3_destination: typing.Union["SsmResourceDataSyncS3Destination", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync aws_ssm_resource_data_sync} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#name SsmResourceDataSync#name}.
        :param s3_destination: s3_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#s3_destination SsmResourceDataSync#s3_destination}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#id SsmResourceDataSync#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmResourceDataSync.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmResourceDataSyncConfig(
            name=name,
            s3_destination=s3_destination,
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

    @jsii.member(jsii_name="putS3Destination")
    def put_s3_destination(
        self,
        *,
        bucket_name: builtins.str,
        region: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        sync_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#bucket_name SsmResourceDataSync#bucket_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#region SsmResourceDataSync#region}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#kms_key_arn SsmResourceDataSync#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#prefix SsmResourceDataSync#prefix}.
        :param sync_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#sync_format SsmResourceDataSync#sync_format}.
        '''
        value = SsmResourceDataSyncS3Destination(
            bucket_name=bucket_name,
            region=region,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
            sync_format=sync_format,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Destination", [value]))

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
    @jsii.member(jsii_name="s3Destination")
    def s3_destination(self) -> "SsmResourceDataSyncS3DestinationOutputReference":
        return typing.cast("SsmResourceDataSyncS3DestinationOutputReference", jsii.get(self, "s3Destination"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3DestinationInput")
    def s3_destination_input(
        self,
    ) -> typing.Optional["SsmResourceDataSyncS3Destination"]:
        return typing.cast(typing.Optional["SsmResourceDataSyncS3Destination"], jsii.get(self, "s3DestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSync, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSync, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmResourceDataSyncConfig",
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
        "s3_destination": "s3Destination",
        "id": "id",
    },
)
class SsmResourceDataSyncConfig(cdktf.TerraformMetaArguments):
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
        s3_destination: typing.Union["SsmResourceDataSyncS3Destination", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#name SsmResourceDataSync#name}.
        :param s3_destination: s3_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#s3_destination SsmResourceDataSync#s3_destination}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#id SsmResourceDataSync#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(s3_destination, dict):
            s3_destination = SsmResourceDataSyncS3Destination(**s3_destination)
        if __debug__:
            type_hints = typing.get_type_hints(SsmResourceDataSyncConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_destination", value=s3_destination, expected_type=type_hints["s3_destination"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "s3_destination": s3_destination,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#name SsmResourceDataSync#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_destination(self) -> "SsmResourceDataSyncS3Destination":
        '''s3_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#s3_destination SsmResourceDataSync#s3_destination}
        '''
        result = self._values.get("s3_destination")
        assert result is not None, "Required property 's3_destination' is missing"
        return typing.cast("SsmResourceDataSyncS3Destination", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#id SsmResourceDataSync#id}.

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
        return "SsmResourceDataSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmResourceDataSyncS3Destination",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "region": "region",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
        "sync_format": "syncFormat",
    },
)
class SsmResourceDataSyncS3Destination:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        region: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        sync_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#bucket_name SsmResourceDataSync#bucket_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#region SsmResourceDataSync#region}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#kms_key_arn SsmResourceDataSync#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#prefix SsmResourceDataSync#prefix}.
        :param sync_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#sync_format SsmResourceDataSync#sync_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmResourceDataSyncS3Destination.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument sync_format", value=sync_format, expected_type=type_hints["sync_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "region": region,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix
        if sync_format is not None:
            self._values["sync_format"] = sync_format

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#bucket_name SsmResourceDataSync#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#region SsmResourceDataSync#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#kms_key_arn SsmResourceDataSync#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#prefix SsmResourceDataSync#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_resource_data_sync#sync_format SsmResourceDataSync#sync_format}.'''
        result = self._values.get("sync_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmResourceDataSyncS3Destination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmResourceDataSyncS3DestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmResourceDataSyncS3DestinationOutputReference",
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
            type_hints = typing.get_type_hints(SsmResourceDataSyncS3DestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetSyncFormat")
    def reset_sync_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncFormat", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="syncFormatInput")
    def sync_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="syncFormat")
    def sync_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncFormat"))

    @sync_format.setter
    def sync_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "sync_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SsmResourceDataSyncS3Destination]:
        return typing.cast(typing.Optional[SsmResourceDataSyncS3Destination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmResourceDataSyncS3Destination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmResourceDataSyncS3DestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmServiceSetting(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ssm.SsmServiceSetting",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting aws_ssm_service_setting}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        setting_id: builtins.str,
        setting_value: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting aws_ssm_service_setting} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param setting_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_id SsmServiceSetting#setting_id}.
        :param setting_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_value SsmServiceSetting#setting_value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#id SsmServiceSetting#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SsmServiceSetting.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmServiceSettingConfig(
            setting_id=setting_id,
            setting_value=setting_value,
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
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="settingIdInput")
    def setting_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingIdInput"))

    @builtins.property
    @jsii.member(jsii_name="settingValueInput")
    def setting_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingValueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmServiceSetting, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="settingId")
    def setting_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingId"))

    @setting_id.setter
    def setting_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmServiceSetting, "setting_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingId", value)

    @builtins.property
    @jsii.member(jsii_name="settingValue")
    def setting_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingValue"))

    @setting_value.setter
    def setting_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SsmServiceSetting, "setting_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ssm.SsmServiceSettingConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "setting_id": "settingId",
        "setting_value": "settingValue",
        "id": "id",
    },
)
class SsmServiceSettingConfig(cdktf.TerraformMetaArguments):
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
        setting_id: builtins.str,
        setting_value: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Systems Manager.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param setting_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_id SsmServiceSetting#setting_id}.
        :param setting_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_value SsmServiceSetting#setting_value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#id SsmServiceSetting#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SsmServiceSettingConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument setting_id", value=setting_id, expected_type=type_hints["setting_id"])
            check_type(argname="argument setting_value", value=setting_value, expected_type=type_hints["setting_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "setting_id": setting_id,
            "setting_value": setting_value,
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
    def setting_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_id SsmServiceSetting#setting_id}.'''
        result = self._values.get("setting_id")
        assert result is not None, "Required property 'setting_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#setting_value SsmServiceSetting#setting_value}.'''
        result = self._values.get("setting_value")
        assert result is not None, "Required property 'setting_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_service_setting#id SsmServiceSetting#id}.

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
        return "SsmServiceSettingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAwsSsmDocument",
    "DataAwsSsmDocumentConfig",
    "DataAwsSsmInstances",
    "DataAwsSsmInstancesConfig",
    "DataAwsSsmInstancesFilter",
    "DataAwsSsmInstancesFilterList",
    "DataAwsSsmInstancesFilterOutputReference",
    "DataAwsSsmMaintenanceWindows",
    "DataAwsSsmMaintenanceWindowsConfig",
    "DataAwsSsmMaintenanceWindowsFilter",
    "DataAwsSsmMaintenanceWindowsFilterList",
    "DataAwsSsmMaintenanceWindowsFilterOutputReference",
    "DataAwsSsmParameter",
    "DataAwsSsmParameterConfig",
    "DataAwsSsmParametersByPath",
    "DataAwsSsmParametersByPathConfig",
    "DataAwsSsmPatchBaseline",
    "DataAwsSsmPatchBaselineApprovalRule",
    "DataAwsSsmPatchBaselineApprovalRuleList",
    "DataAwsSsmPatchBaselineApprovalRuleOutputReference",
    "DataAwsSsmPatchBaselineApprovalRulePatchFilter",
    "DataAwsSsmPatchBaselineApprovalRulePatchFilterList",
    "DataAwsSsmPatchBaselineApprovalRulePatchFilterOutputReference",
    "DataAwsSsmPatchBaselineConfig",
    "DataAwsSsmPatchBaselineGlobalFilter",
    "DataAwsSsmPatchBaselineGlobalFilterList",
    "DataAwsSsmPatchBaselineGlobalFilterOutputReference",
    "DataAwsSsmPatchBaselineSource",
    "DataAwsSsmPatchBaselineSourceList",
    "DataAwsSsmPatchBaselineSourceOutputReference",
    "SsmActivation",
    "SsmActivationConfig",
    "SsmAssociation",
    "SsmAssociationConfig",
    "SsmAssociationOutputLocation",
    "SsmAssociationOutputLocationOutputReference",
    "SsmAssociationTargets",
    "SsmAssociationTargetsList",
    "SsmAssociationTargetsOutputReference",
    "SsmDocument",
    "SsmDocumentAttachmentsSource",
    "SsmDocumentAttachmentsSourceList",
    "SsmDocumentAttachmentsSourceOutputReference",
    "SsmDocumentConfig",
    "SsmDocumentParameter",
    "SsmDocumentParameterList",
    "SsmDocumentParameterOutputReference",
    "SsmMaintenanceWindow",
    "SsmMaintenanceWindowConfig",
    "SsmMaintenanceWindowTarget",
    "SsmMaintenanceWindowTargetConfig",
    "SsmMaintenanceWindowTargetTargets",
    "SsmMaintenanceWindowTargetTargetsList",
    "SsmMaintenanceWindowTargetTargetsOutputReference",
    "SsmMaintenanceWindowTask",
    "SsmMaintenanceWindowTaskConfig",
    "SsmMaintenanceWindowTaskTargets",
    "SsmMaintenanceWindowTaskTargetsList",
    "SsmMaintenanceWindowTaskTargetsOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference",
    "SsmParameter",
    "SsmParameterConfig",
    "SsmPatchBaseline",
    "SsmPatchBaselineApprovalRule",
    "SsmPatchBaselineApprovalRuleList",
    "SsmPatchBaselineApprovalRuleOutputReference",
    "SsmPatchBaselineApprovalRulePatchFilter",
    "SsmPatchBaselineApprovalRulePatchFilterList",
    "SsmPatchBaselineApprovalRulePatchFilterOutputReference",
    "SsmPatchBaselineConfig",
    "SsmPatchBaselineGlobalFilter",
    "SsmPatchBaselineGlobalFilterList",
    "SsmPatchBaselineGlobalFilterOutputReference",
    "SsmPatchBaselineSource",
    "SsmPatchBaselineSourceList",
    "SsmPatchBaselineSourceOutputReference",
    "SsmPatchGroup",
    "SsmPatchGroupConfig",
    "SsmResourceDataSync",
    "SsmResourceDataSyncConfig",
    "SsmResourceDataSyncS3Destination",
    "SsmResourceDataSyncS3DestinationOutputReference",
    "SsmServiceSetting",
    "SsmServiceSettingConfig",
]

publication.publish()
