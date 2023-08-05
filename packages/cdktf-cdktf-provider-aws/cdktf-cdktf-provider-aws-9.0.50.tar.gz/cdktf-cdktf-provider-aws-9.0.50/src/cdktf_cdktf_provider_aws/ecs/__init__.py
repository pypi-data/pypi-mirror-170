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


class DataAwsEcsCluster(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster aws_ecs_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster aws_ecs_cluster} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#cluster_name DataAwsEcsCluster#cluster_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#id DataAwsEcsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsEcsClusterConfig(
            cluster_name=cluster_name,
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
    @jsii.member(jsii_name="pendingTasksCount")
    def pending_tasks_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pendingTasksCount"))

    @builtins.property
    @jsii.member(jsii_name="registeredContainerInstancesCount")
    def registered_container_instances_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "registeredContainerInstancesCount"))

    @builtins.property
    @jsii.member(jsii_name="runningTasksCount")
    def running_tasks_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "runningTasksCount"))

    @builtins.property
    @jsii.member(jsii_name="setting")
    def setting(self) -> "DataAwsEcsClusterSettingList":
        return typing.cast("DataAwsEcsClusterSettingList", jsii.get(self, "setting"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsCluster, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_name": "clusterName",
        "id": "id",
    },
)
class DataAwsEcsClusterConfig(cdktf.TerraformMetaArguments):
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
        cluster_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#cluster_name DataAwsEcsCluster#cluster_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#id DataAwsEcsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
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
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#cluster_name DataAwsEcsCluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_cluster#id DataAwsEcsCluster#id}.

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
        return "DataAwsEcsClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsClusterSetting",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsEcsClusterSetting:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEcsClusterSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEcsClusterSettingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsClusterSettingList",
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
            type_hints = typing.get_type_hints(DataAwsEcsClusterSettingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsEcsClusterSettingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsClusterSettingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsEcsClusterSettingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsClusterSettingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsEcsClusterSettingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsEcsClusterSettingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsEcsClusterSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsClusterSettingOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsEcsClusterSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsEcsClusterSetting]:
        return typing.cast(typing.Optional[DataAwsEcsClusterSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsEcsClusterSetting]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsClusterSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsEcsContainerDefinition(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsContainerDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition aws_ecs_container_definition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_name: builtins.str,
        task_definition: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition aws_ecs_container_definition} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#container_name DataAwsEcsContainerDefinition#container_name}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#task_definition DataAwsEcsContainerDefinition#task_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#id DataAwsEcsContainerDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsContainerDefinition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsEcsContainerDefinitionConfig(
            container_name=container_name,
            task_definition=task_definition,
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
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @builtins.property
    @jsii.member(jsii_name="disableNetworking")
    def disable_networking(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "disableNetworking"))

    @builtins.property
    @jsii.member(jsii_name="dockerLabels")
    def docker_labels(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "dockerLabels"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="imageDigest")
    def image_digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageDigest"))

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @builtins.property
    @jsii.member(jsii_name="memoryReservation")
    def memory_reservation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryReservation"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsContainerDefinition, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsContainerDefinition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsContainerDefinition, "task_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsContainerDefinitionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_name": "containerName",
        "task_definition": "taskDefinition",
        "id": "id",
    },
)
class DataAwsEcsContainerDefinitionConfig(cdktf.TerraformMetaArguments):
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
        container_name: builtins.str,
        task_definition: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#container_name DataAwsEcsContainerDefinition#container_name}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#task_definition DataAwsEcsContainerDefinition#task_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#id DataAwsEcsContainerDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsContainerDefinitionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
            "task_definition": task_definition,
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
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#container_name DataAwsEcsContainerDefinition#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#task_definition DataAwsEcsContainerDefinition#task_definition}.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_container_definition#id DataAwsEcsContainerDefinition#id}.

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
        return "DataAwsEcsContainerDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEcsService(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ecs_service aws_ecs_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_arn: builtins.str,
        service_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ecs_service aws_ecs_service} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#cluster_arn DataAwsEcsService#cluster_arn}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#service_name DataAwsEcsService#service_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#id DataAwsEcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#tags DataAwsEcsService#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsEcsServiceConfig(
            cluster_arn=cluster_arn,
            service_name=service_name,
            id=id,
            tags=tags,
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

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCount"))

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategy")
    def scheduling_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingStrategy"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @builtins.property
    @jsii.member(jsii_name="clusterArnInput")
    def cluster_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsService, "cluster_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsService, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsService, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_arn": "clusterArn",
        "service_name": "serviceName",
        "id": "id",
        "tags": "tags",
    },
)
class DataAwsEcsServiceConfig(cdktf.TerraformMetaArguments):
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
        cluster_arn: builtins.str,
        service_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#cluster_arn DataAwsEcsService#cluster_arn}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#service_name DataAwsEcsService#service_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#id DataAwsEcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#tags DataAwsEcsService#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "service_name": service_name,
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
        if tags is not None:
            self._values["tags"] = tags

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
    def cluster_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#cluster_arn DataAwsEcsService#cluster_arn}.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#service_name DataAwsEcsService#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#id DataAwsEcsService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_service#tags DataAwsEcsService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsEcsServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsEcsTaskDefinition(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsTaskDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition aws_ecs_task_definition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        task_definition: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition aws_ecs_task_definition} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#task_definition DataAwsEcsTaskDefinition#task_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#id DataAwsEcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsTaskDefinition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsEcsTaskDefinitionConfig(
            task_definition=task_definition,
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
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="taskRoleArn")
    def task_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsTaskDefinition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsEcsTaskDefinition, "task_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.DataAwsEcsTaskDefinitionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "task_definition": "taskDefinition",
        "id": "id",
    },
)
class DataAwsEcsTaskDefinitionConfig(cdktf.TerraformMetaArguments):
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
        task_definition: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#task_definition DataAwsEcsTaskDefinition#task_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#id DataAwsEcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsEcsTaskDefinitionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "task_definition": task_definition,
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
    def task_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#task_definition DataAwsEcsTaskDefinition#task_definition}.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ecs_task_definition#id DataAwsEcsTaskDefinition#id}.

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
        return "DataAwsEcsTaskDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsAccountSettingDefault(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsAccountSettingDefault",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default aws_ecs_account_setting_default}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        value: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default aws_ecs_account_setting_default} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#name EcsAccountSettingDefault#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#value EcsAccountSettingDefault#value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#id EcsAccountSettingDefault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsAccountSettingDefault.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsAccountSettingDefaultConfig(
            name=name,
            value=value,
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
    @jsii.member(jsii_name="principalArn")
    def principal_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalArn"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsAccountSettingDefault, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsAccountSettingDefault, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsAccountSettingDefault, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsAccountSettingDefaultConfig",
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
        "value": "value",
        "id": "id",
    },
)
class EcsAccountSettingDefaultConfig(cdktf.TerraformMetaArguments):
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
        value: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#name EcsAccountSettingDefault#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#value EcsAccountSettingDefault#value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#id EcsAccountSettingDefault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(EcsAccountSettingDefaultConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#name EcsAccountSettingDefault#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#value EcsAccountSettingDefault#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_account_setting_default#id EcsAccountSettingDefault#id}.

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
        return "EcsAccountSettingDefaultConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsCapacityProvider(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider aws_ecs_capacity_provider}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        auto_scaling_group_provider: typing.Union["EcsCapacityProviderAutoScalingGroupProvider", typing.Dict[str, typing.Any]],
        name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider aws_ecs_capacity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auto_scaling_group_provider: auto_scaling_group_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsCapacityProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsCapacityProviderConfig(
            auto_scaling_group_provider=auto_scaling_group_provider,
            name=name,
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

    @jsii.member(jsii_name="putAutoScalingGroupProvider")
    def put_auto_scaling_group_provider(
        self,
        *,
        auto_scaling_group_arn: builtins.str,
        managed_scaling: typing.Optional[typing.Union["EcsCapacityProviderAutoScalingGroupProviderManagedScaling", typing.Dict[str, typing.Any]]] = None,
        managed_termination_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.
        :param managed_scaling: managed_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        :param managed_termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.
        '''
        value = EcsCapacityProviderAutoScalingGroupProvider(
            auto_scaling_group_arn=auto_scaling_group_arn,
            managed_scaling=managed_scaling,
            managed_termination_protection=managed_termination_protection,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScalingGroupProvider", [value]))

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
    @jsii.member(jsii_name="autoScalingGroupProvider")
    def auto_scaling_group_provider(
        self,
    ) -> "EcsCapacityProviderAutoScalingGroupProviderOutputReference":
        return typing.cast("EcsCapacityProviderAutoScalingGroupProviderOutputReference", jsii.get(self, "autoScalingGroupProvider"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupProviderInput")
    def auto_scaling_group_provider_input(
        self,
    ) -> typing.Optional["EcsCapacityProviderAutoScalingGroupProvider"]:
        return typing.cast(typing.Optional["EcsCapacityProviderAutoScalingGroupProvider"], jsii.get(self, "autoScalingGroupProviderInput"))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProvider, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProvider, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProvider, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProvider, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProviderAutoScalingGroupProvider",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group_arn": "autoScalingGroupArn",
        "managed_scaling": "managedScaling",
        "managed_termination_protection": "managedTerminationProtection",
    },
)
class EcsCapacityProviderAutoScalingGroupProvider:
    def __init__(
        self,
        *,
        auto_scaling_group_arn: builtins.str,
        managed_scaling: typing.Optional[typing.Union["EcsCapacityProviderAutoScalingGroupProviderManagedScaling", typing.Dict[str, typing.Any]]] = None,
        managed_termination_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.
        :param managed_scaling: managed_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        :param managed_termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.
        '''
        if isinstance(managed_scaling, dict):
            managed_scaling = EcsCapacityProviderAutoScalingGroupProviderManagedScaling(**managed_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(EcsCapacityProviderAutoScalingGroupProvider.__init__)
            check_type(argname="argument auto_scaling_group_arn", value=auto_scaling_group_arn, expected_type=type_hints["auto_scaling_group_arn"])
            check_type(argname="argument managed_scaling", value=managed_scaling, expected_type=type_hints["managed_scaling"])
            check_type(argname="argument managed_termination_protection", value=managed_termination_protection, expected_type=type_hints["managed_termination_protection"])
        self._values: typing.Dict[str, typing.Any] = {
            "auto_scaling_group_arn": auto_scaling_group_arn,
        }
        if managed_scaling is not None:
            self._values["managed_scaling"] = managed_scaling
        if managed_termination_protection is not None:
            self._values["managed_termination_protection"] = managed_termination_protection

    @builtins.property
    def auto_scaling_group_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.'''
        result = self._values.get("auto_scaling_group_arn")
        assert result is not None, "Required property 'auto_scaling_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_scaling(
        self,
    ) -> typing.Optional["EcsCapacityProviderAutoScalingGroupProviderManagedScaling"]:
        '''managed_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        '''
        result = self._values.get("managed_scaling")
        return typing.cast(typing.Optional["EcsCapacityProviderAutoScalingGroupProviderManagedScaling"], result)

    @builtins.property
    def managed_termination_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.'''
        result = self._values.get("managed_termination_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderAutoScalingGroupProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProviderAutoScalingGroupProviderManagedScaling",
    jsii_struct_bases=[],
    name_mapping={
        "instance_warmup_period": "instanceWarmupPeriod",
        "maximum_scaling_step_size": "maximumScalingStepSize",
        "minimum_scaling_step_size": "minimumScalingStepSize",
        "status": "status",
        "target_capacity": "targetCapacity",
    },
)
class EcsCapacityProviderAutoScalingGroupProviderManagedScaling:
    def __init__(
        self,
        *,
        instance_warmup_period: typing.Optional[jsii.Number] = None,
        maximum_scaling_step_size: typing.Optional[jsii.Number] = None,
        minimum_scaling_step_size: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_warmup_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.
        :param maximum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.
        :param minimum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsCapacityProviderAutoScalingGroupProviderManagedScaling.__init__)
            check_type(argname="argument instance_warmup_period", value=instance_warmup_period, expected_type=type_hints["instance_warmup_period"])
            check_type(argname="argument maximum_scaling_step_size", value=maximum_scaling_step_size, expected_type=type_hints["maximum_scaling_step_size"])
            check_type(argname="argument minimum_scaling_step_size", value=minimum_scaling_step_size, expected_type=type_hints["minimum_scaling_step_size"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument target_capacity", value=target_capacity, expected_type=type_hints["target_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_warmup_period is not None:
            self._values["instance_warmup_period"] = instance_warmup_period
        if maximum_scaling_step_size is not None:
            self._values["maximum_scaling_step_size"] = maximum_scaling_step_size
        if minimum_scaling_step_size is not None:
            self._values["minimum_scaling_step_size"] = minimum_scaling_step_size
        if status is not None:
            self._values["status"] = status
        if target_capacity is not None:
            self._values["target_capacity"] = target_capacity

    @builtins.property
    def instance_warmup_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.'''
        result = self._values.get("instance_warmup_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_scaling_step_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.'''
        result = self._values.get("maximum_scaling_step_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_scaling_step_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.'''
        result = self._values.get("minimum_scaling_step_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.'''
        result = self._values.get("target_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderAutoScalingGroupProviderManagedScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference",
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
            type_hints = typing.get_type_hints(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceWarmupPeriod")
    def reset_instance_warmup_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceWarmupPeriod", []))

    @jsii.member(jsii_name="resetMaximumScalingStepSize")
    def reset_maximum_scaling_step_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumScalingStepSize", []))

    @jsii.member(jsii_name="resetMinimumScalingStepSize")
    def reset_minimum_scaling_step_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumScalingStepSize", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTargetCapacity")
    def reset_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupPeriodInput")
    def instance_warmup_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceWarmupPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumScalingStepSizeInput")
    def maximum_scaling_step_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumScalingStepSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumScalingStepSizeInput")
    def minimum_scaling_step_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumScalingStepSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCapacityInput")
    def target_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupPeriod")
    def instance_warmup_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceWarmupPeriod"))

    @instance_warmup_period.setter
    def instance_warmup_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "instance_warmup_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceWarmupPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maximumScalingStepSize")
    def maximum_scaling_step_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumScalingStepSize"))

    @maximum_scaling_step_size.setter
    def maximum_scaling_step_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "maximum_scaling_step_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumScalingStepSize", value)

    @builtins.property
    @jsii.member(jsii_name="minimumScalingStepSize")
    def minimum_scaling_step_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumScalingStepSize"))

    @minimum_scaling_step_size.setter
    def minimum_scaling_step_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "minimum_scaling_step_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumScalingStepSize", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="targetCapacity")
    def target_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetCapacity"))

    @target_capacity.setter
    def target_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "target_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsCapacityProviderAutoScalingGroupProviderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProviderAutoScalingGroupProviderOutputReference",
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
            type_hints = typing.get_type_hints(EcsCapacityProviderAutoScalingGroupProviderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putManagedScaling")
    def put_managed_scaling(
        self,
        *,
        instance_warmup_period: typing.Optional[jsii.Number] = None,
        maximum_scaling_step_size: typing.Optional[jsii.Number] = None,
        minimum_scaling_step_size: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_warmup_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.
        :param maximum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.
        :param minimum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.
        '''
        value = EcsCapacityProviderAutoScalingGroupProviderManagedScaling(
            instance_warmup_period=instance_warmup_period,
            maximum_scaling_step_size=maximum_scaling_step_size,
            minimum_scaling_step_size=minimum_scaling_step_size,
            status=status,
            target_capacity=target_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putManagedScaling", [value]))

    @jsii.member(jsii_name="resetManagedScaling")
    def reset_managed_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedScaling", []))

    @jsii.member(jsii_name="resetManagedTerminationProtection")
    def reset_managed_termination_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedTerminationProtection", []))

    @builtins.property
    @jsii.member(jsii_name="managedScaling")
    def managed_scaling(
        self,
    ) -> EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference:
        return typing.cast(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, jsii.get(self, "managedScaling"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupArnInput")
    def auto_scaling_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="managedScalingInput")
    def managed_scaling_input(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling], jsii.get(self, "managedScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="managedTerminationProtectionInput")
    def managed_termination_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedTerminationProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoScalingGroupArn"))

    @auto_scaling_group_arn.setter
    def auto_scaling_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderOutputReference, "auto_scaling_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="managedTerminationProtection")
    def managed_termination_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedTerminationProtection"))

    @managed_termination_protection.setter
    def managed_termination_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderOutputReference, "managed_termination_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedTerminationProtection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProvider]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProvider], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsCapacityProviderAutoScalingGroupProvider],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCapacityProviderAutoScalingGroupProviderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsCapacityProviderConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auto_scaling_group_provider": "autoScalingGroupProvider",
        "name": "name",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class EcsCapacityProviderConfig(cdktf.TerraformMetaArguments):
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
        auto_scaling_group_provider: typing.Union[EcsCapacityProviderAutoScalingGroupProvider, typing.Dict[str, typing.Any]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auto_scaling_group_provider: auto_scaling_group_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_scaling_group_provider, dict):
            auto_scaling_group_provider = EcsCapacityProviderAutoScalingGroupProvider(**auto_scaling_group_provider)
        if __debug__:
            type_hints = typing.get_type_hints(EcsCapacityProviderConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auto_scaling_group_provider", value=auto_scaling_group_provider, expected_type=type_hints["auto_scaling_group_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "auto_scaling_group_provider": auto_scaling_group_provider,
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
    def auto_scaling_group_provider(
        self,
    ) -> EcsCapacityProviderAutoScalingGroupProvider:
        '''auto_scaling_group_provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        '''
        result = self._values.get("auto_scaling_group_provider")
        assert result is not None, "Required property 'auto_scaling_group_provider' is missing"
        return typing.cast(EcsCapacityProviderAutoScalingGroupProvider, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster aws_ecs_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        capacity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[typing.Union["EcsClusterConfiguration", typing.Dict[str, typing.Any]]] = None,
        default_capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        setting: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterSetting", typing.Dict[str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster aws_ecs_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#name EcsCluster#name}.
        :param capacity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#capacity_providers EcsCluster#capacity_providers}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#configuration EcsCluster#configuration}
        :param default_capacity_provider_strategy: default_capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#default_capacity_provider_strategy EcsCluster#default_capacity_provider_strategy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#id EcsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param setting: setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#setting EcsCluster#setting}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags EcsCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags_all EcsCluster#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsClusterConfig(
            name=name,
            capacity_providers=capacity_providers,
            configuration=configuration,
            default_capacity_provider_strategy=default_capacity_provider_strategy,
            id=id,
            setting=setting,
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

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        *,
        execute_command_configuration: typing.Optional[typing.Union["EcsClusterConfigurationExecuteCommandConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execute_command_configuration: execute_command_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#execute_command_configuration EcsCluster#execute_command_configuration}
        '''
        value = EcsClusterConfiguration(
            execute_command_configuration=execute_command_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putDefaultCapacityProviderStrategy")
    def put_default_capacity_provider_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsCluster.put_default_capacity_provider_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putSetting")
    def put_setting(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterSetting", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsCluster.put_setting)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSetting", [value]))

    @jsii.member(jsii_name="resetCapacityProviders")
    def reset_capacity_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviders", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetDefaultCapacityProviderStrategy")
    def reset_default_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSetting")
    def reset_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetting", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "EcsClusterConfigurationOutputReference":
        return typing.cast("EcsClusterConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="defaultCapacityProviderStrategy")
    def default_capacity_provider_strategy(
        self,
    ) -> "EcsClusterDefaultCapacityProviderStrategyList":
        return typing.cast("EcsClusterDefaultCapacityProviderStrategyList", jsii.get(self, "defaultCapacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="setting")
    def setting(self) -> "EcsClusterSettingList":
        return typing.cast("EcsClusterSettingList", jsii.get(self, "setting"))

    @builtins.property
    @jsii.member(jsii_name="capacityProvidersInput")
    def capacity_providers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capacityProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional["EcsClusterConfiguration"]:
        return typing.cast(typing.Optional["EcsClusterConfiguration"], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCapacityProviderStrategyInput")
    def default_capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterDefaultCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterDefaultCapacityProviderStrategy"]]], jsii.get(self, "defaultCapacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="settingInput")
    def setting_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterSetting"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterSetting"]]], jsii.get(self, "settingInput"))

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
    @jsii.member(jsii_name="capacityProviders")
    def capacity_providers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "capacityProviders"))

    @capacity_providers.setter
    def capacity_providers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCluster, "capacity_providers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProviders", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsCluster, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


class EcsClusterCapacityProviders(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterCapacityProviders",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers aws_ecs_cluster_capacity_providers}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_name: builtins.str,
        capacity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers aws_ecs_cluster_capacity_providers} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#cluster_name EcsClusterCapacityProviders#cluster_name}.
        :param capacity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#capacity_providers EcsClusterCapacityProviders#capacity_providers}.
        :param default_capacity_provider_strategy: default_capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#default_capacity_provider_strategy EcsClusterCapacityProviders#default_capacity_provider_strategy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#id EcsClusterCapacityProviders#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterCapacityProviders.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsClusterCapacityProvidersConfig(
            cluster_name=cluster_name,
            capacity_providers=capacity_providers,
            default_capacity_provider_strategy=default_capacity_provider_strategy,
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

    @jsii.member(jsii_name="putDefaultCapacityProviderStrategy")
    def put_default_capacity_provider_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterCapacityProviders.put_default_capacity_provider_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="resetCapacityProviders")
    def reset_capacity_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviders", []))

    @jsii.member(jsii_name="resetDefaultCapacityProviderStrategy")
    def reset_default_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultCapacityProviderStrategy", []))

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
    @jsii.member(jsii_name="defaultCapacityProviderStrategy")
    def default_capacity_provider_strategy(
        self,
    ) -> "EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList":
        return typing.cast("EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList", jsii.get(self, "defaultCapacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="capacityProvidersInput")
    def capacity_providers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capacityProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCapacityProviderStrategyInput")
    def default_capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy"]]], jsii.get(self, "defaultCapacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviders")
    def capacity_providers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "capacityProviders"))

    @capacity_providers.setter
    def capacity_providers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProviders, "capacity_providers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProviders", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProviders, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProviders, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterCapacityProvidersConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_name": "clusterName",
        "capacity_providers": "capacityProviders",
        "default_capacity_provider_strategy": "defaultCapacityProviderStrategy",
        "id": "id",
    },
)
class EcsClusterCapacityProvidersConfig(cdktf.TerraformMetaArguments):
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
        cluster_name: builtins.str,
        capacity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#cluster_name EcsClusterCapacityProviders#cluster_name}.
        :param capacity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#capacity_providers EcsClusterCapacityProviders#capacity_providers}.
        :param default_capacity_provider_strategy: default_capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#default_capacity_provider_strategy EcsClusterCapacityProviders#default_capacity_provider_strategy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#id EcsClusterCapacityProviders#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterCapacityProvidersConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument capacity_providers", value=capacity_providers, expected_type=type_hints["capacity_providers"])
            check_type(argname="argument default_capacity_provider_strategy", value=default_capacity_provider_strategy, expected_type=type_hints["default_capacity_provider_strategy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
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
        if capacity_providers is not None:
            self._values["capacity_providers"] = capacity_providers
        if default_capacity_provider_strategy is not None:
            self._values["default_capacity_provider_strategy"] = default_capacity_provider_strategy
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
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#cluster_name EcsClusterCapacityProviders#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_providers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#capacity_providers EcsClusterCapacityProviders#capacity_providers}.'''
        result = self._values.get("capacity_providers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy"]]]:
        '''default_capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#default_capacity_provider_strategy EcsClusterCapacityProviders#default_capacity_provider_strategy}
        '''
        result = self._values.get("default_capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterCapacityProvidersDefaultCapacityProviderStrategy"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#id EcsClusterCapacityProviders#id}.

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
        return "EcsClusterCapacityProvidersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterCapacityProvidersDefaultCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class EcsClusterCapacityProvidersDefaultCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#capacity_provider EcsClusterCapacityProviders#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#base EcsClusterCapacityProviders#base}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#weight EcsClusterCapacityProviders#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterCapacityProvidersDefaultCapacityProviderStrategy.__init__)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#capacity_provider EcsClusterCapacityProviders#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#base EcsClusterCapacityProviders#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster_capacity_providers#weight EcsClusterCapacityProviders#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterCapacityProvidersDefaultCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference, "base").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference, "capacity_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsClusterCapacityProvidersDefaultCapacityProviderStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfig",
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
        "capacity_providers": "capacityProviders",
        "configuration": "configuration",
        "default_capacity_provider_strategy": "defaultCapacityProviderStrategy",
        "id": "id",
        "setting": "setting",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class EcsClusterConfig(cdktf.TerraformMetaArguments):
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
        capacity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[typing.Union["EcsClusterConfiguration", typing.Dict[str, typing.Any]]] = None,
        default_capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterDefaultCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        setting: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsClusterSetting", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#name EcsCluster#name}.
        :param capacity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#capacity_providers EcsCluster#capacity_providers}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#configuration EcsCluster#configuration}
        :param default_capacity_provider_strategy: default_capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#default_capacity_provider_strategy EcsCluster#default_capacity_provider_strategy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#id EcsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param setting: setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#setting EcsCluster#setting}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags EcsCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags_all EcsCluster#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = EcsClusterConfiguration(**configuration)
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capacity_providers", value=capacity_providers, expected_type=type_hints["capacity_providers"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument default_capacity_provider_strategy", value=default_capacity_provider_strategy, expected_type=type_hints["default_capacity_provider_strategy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument setting", value=setting, expected_type=type_hints["setting"])
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
        if capacity_providers is not None:
            self._values["capacity_providers"] = capacity_providers
        if configuration is not None:
            self._values["configuration"] = configuration
        if default_capacity_provider_strategy is not None:
            self._values["default_capacity_provider_strategy"] = default_capacity_provider_strategy
        if id is not None:
            self._values["id"] = id
        if setting is not None:
            self._values["setting"] = setting
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#name EcsCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_providers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#capacity_providers EcsCluster#capacity_providers}.'''
        result = self._values.get("capacity_providers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def configuration(self) -> typing.Optional["EcsClusterConfiguration"]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#configuration EcsCluster#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional["EcsClusterConfiguration"], result)

    @builtins.property
    def default_capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterDefaultCapacityProviderStrategy"]]]:
        '''default_capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#default_capacity_provider_strategy EcsCluster#default_capacity_provider_strategy}
        '''
        result = self._values.get("default_capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterDefaultCapacityProviderStrategy"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#id EcsCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def setting(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterSetting"]]]:
        '''setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#setting EcsCluster#setting}
        '''
        result = self._values.get("setting")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsClusterSetting"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags EcsCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#tags_all EcsCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfiguration",
    jsii_struct_bases=[],
    name_mapping={"execute_command_configuration": "executeCommandConfiguration"},
)
class EcsClusterConfiguration:
    def __init__(
        self,
        *,
        execute_command_configuration: typing.Optional[typing.Union["EcsClusterConfigurationExecuteCommandConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execute_command_configuration: execute_command_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#execute_command_configuration EcsCluster#execute_command_configuration}
        '''
        if isinstance(execute_command_configuration, dict):
            execute_command_configuration = EcsClusterConfigurationExecuteCommandConfiguration(**execute_command_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterConfiguration.__init__)
            check_type(argname="argument execute_command_configuration", value=execute_command_configuration, expected_type=type_hints["execute_command_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if execute_command_configuration is not None:
            self._values["execute_command_configuration"] = execute_command_configuration

    @builtins.property
    def execute_command_configuration(
        self,
    ) -> typing.Optional["EcsClusterConfigurationExecuteCommandConfiguration"]:
        '''execute_command_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#execute_command_configuration EcsCluster#execute_command_configuration}
        '''
        result = self._values.get("execute_command_configuration")
        return typing.cast(typing.Optional["EcsClusterConfigurationExecuteCommandConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfigurationExecuteCommandConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "kms_key_id": "kmsKeyId",
        "log_configuration": "logConfiguration",
        "logging": "logging",
    },
)
class EcsClusterConfigurationExecuteCommandConfiguration:
    def __init__(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_configuration: typing.Optional[typing.Union["EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#kms_key_id EcsCluster#kms_key_id}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#log_configuration EcsCluster#log_configuration}
        :param logging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#logging EcsCluster#logging}.
        '''
        if isinstance(log_configuration, dict):
            log_configuration = EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration(**log_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterConfigurationExecuteCommandConfiguration.__init__)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if logging is not None:
            self._values["logging"] = logging

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#kms_key_id EcsCluster#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional["EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration"]:
        '''log_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#log_configuration EcsCluster#log_configuration}
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional["EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration"], result)

    @builtins.property
    def logging(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#logging EcsCluster#logging}.'''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterConfigurationExecuteCommandConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_encryption_enabled": "cloudWatchEncryptionEnabled",
        "cloud_watch_log_group_name": "cloudWatchLogGroupName",
        "s3_bucket_encryption_enabled": "s3BucketEncryptionEnabled",
        "s3_bucket_name": "s3BucketName",
        "s3_key_prefix": "s3KeyPrefix",
    },
)
class EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration:
    def __init__(
        self,
        *,
        cloud_watch_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cloud_watch_log_group_name: typing.Optional[builtins.str] = None,
        s3_bucket_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        s3_bucket_name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_watch_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_encryption_enabled EcsCluster#cloud_watch_encryption_enabled}.
        :param cloud_watch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_log_group_name EcsCluster#cloud_watch_log_group_name}.
        :param s3_bucket_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_encryption_enabled EcsCluster#s3_bucket_encryption_enabled}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_name EcsCluster#s3_bucket_name}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_key_prefix EcsCluster#s3_key_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration.__init__)
            check_type(argname="argument cloud_watch_encryption_enabled", value=cloud_watch_encryption_enabled, expected_type=type_hints["cloud_watch_encryption_enabled"])
            check_type(argname="argument cloud_watch_log_group_name", value=cloud_watch_log_group_name, expected_type=type_hints["cloud_watch_log_group_name"])
            check_type(argname="argument s3_bucket_encryption_enabled", value=s3_bucket_encryption_enabled, expected_type=type_hints["s3_bucket_encryption_enabled"])
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_watch_encryption_enabled is not None:
            self._values["cloud_watch_encryption_enabled"] = cloud_watch_encryption_enabled
        if cloud_watch_log_group_name is not None:
            self._values["cloud_watch_log_group_name"] = cloud_watch_log_group_name
        if s3_bucket_encryption_enabled is not None:
            self._values["s3_bucket_encryption_enabled"] = s3_bucket_encryption_enabled
        if s3_bucket_name is not None:
            self._values["s3_bucket_name"] = s3_bucket_name
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix

    @builtins.property
    def cloud_watch_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_encryption_enabled EcsCluster#cloud_watch_encryption_enabled}.'''
        result = self._values.get("cloud_watch_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cloud_watch_log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_log_group_name EcsCluster#cloud_watch_log_group_name}.'''
        result = self._values.get("cloud_watch_log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_bucket_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_encryption_enabled EcsCluster#s3_bucket_encryption_enabled}.'''
        result = self._values.get("s3_bucket_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def s3_bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_name EcsCluster#s3_bucket_name}.'''
        result = self._values.get("s3_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_key_prefix EcsCluster#s3_key_prefix}.'''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudWatchEncryptionEnabled")
    def reset_cloud_watch_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchEncryptionEnabled", []))

    @jsii.member(jsii_name="resetCloudWatchLogGroupName")
    def reset_cloud_watch_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchLogGroupName", []))

    @jsii.member(jsii_name="resetS3BucketEncryptionEnabled")
    def reset_s3_bucket_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BucketEncryptionEnabled", []))

    @jsii.member(jsii_name="resetS3BucketName")
    def reset_s3_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BucketName", []))

    @jsii.member(jsii_name="resetS3KeyPrefix")
    def reset_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KeyPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchEncryptionEnabledInput")
    def cloud_watch_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cloudWatchEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupNameInput")
    def cloud_watch_log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketEncryptionEnabledInput")
    def s3_bucket_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "s3BucketEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketNameInput")
    def s3_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefixInput")
    def s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchEncryptionEnabled")
    def cloud_watch_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cloudWatchEncryptionEnabled"))

    @cloud_watch_encryption_enabled.setter
    def cloud_watch_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "cloud_watch_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupName")
    def cloud_watch_log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupName"))

    @cloud_watch_log_group_name.setter
    def cloud_watch_log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "cloud_watch_log_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketEncryptionEnabled")
    def s3_bucket_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "s3BucketEncryptionEnabled"))

    @s3_bucket_encryption_enabled.setter
    def s3_bucket_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "s3_bucket_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "s3_bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "s3_key_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsClusterConfigurationExecuteCommandConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfigurationExecuteCommandConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterConfigurationExecuteCommandConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogConfiguration")
    def put_log_configuration(
        self,
        *,
        cloud_watch_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cloud_watch_log_group_name: typing.Optional[builtins.str] = None,
        s3_bucket_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        s3_bucket_name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_watch_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_encryption_enabled EcsCluster#cloud_watch_encryption_enabled}.
        :param cloud_watch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#cloud_watch_log_group_name EcsCluster#cloud_watch_log_group_name}.
        :param s3_bucket_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_encryption_enabled EcsCluster#s3_bucket_encryption_enabled}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_bucket_name EcsCluster#s3_bucket_name}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#s3_key_prefix EcsCluster#s3_key_prefix}.
        '''
        value = EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration(
            cloud_watch_encryption_enabled=cloud_watch_encryption_enabled,
            cloud_watch_log_group_name=cloud_watch_log_group_name,
            s3_bucket_encryption_enabled=s3_bucket_encryption_enabled,
            s3_bucket_name=s3_bucket_name,
            s3_key_prefix=s3_key_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfiguration", [value]))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetLogConfiguration")
    def reset_log_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfiguration", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference:
        return typing.cast(EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference, jsii.get(self, "logConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigurationInput")
    def log_configuration_input(
        self,
    ) -> typing.Optional[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration], jsii.get(self, "logConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationOutputReference, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logging"))

    @logging.setter
    def logging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationOutputReference, "logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsClusterConfigurationExecuteCommandConfiguration]:
        return typing.cast(typing.Optional[EcsClusterConfigurationExecuteCommandConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsClusterConfigurationExecuteCommandConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationExecuteCommandConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsClusterConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExecuteCommandConfiguration")
    def put_execute_command_configuration(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_configuration: typing.Optional[typing.Union[EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration, typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#kms_key_id EcsCluster#kms_key_id}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#log_configuration EcsCluster#log_configuration}
        :param logging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#logging EcsCluster#logging}.
        '''
        value = EcsClusterConfigurationExecuteCommandConfiguration(
            kms_key_id=kms_key_id, log_configuration=log_configuration, logging=logging
        )

        return typing.cast(None, jsii.invoke(self, "putExecuteCommandConfiguration", [value]))

    @jsii.member(jsii_name="resetExecuteCommandConfiguration")
    def reset_execute_command_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecuteCommandConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="executeCommandConfiguration")
    def execute_command_configuration(
        self,
    ) -> EcsClusterConfigurationExecuteCommandConfigurationOutputReference:
        return typing.cast(EcsClusterConfigurationExecuteCommandConfigurationOutputReference, jsii.get(self, "executeCommandConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="executeCommandConfigurationInput")
    def execute_command_configuration_input(
        self,
    ) -> typing.Optional[EcsClusterConfigurationExecuteCommandConfiguration]:
        return typing.cast(typing.Optional[EcsClusterConfigurationExecuteCommandConfiguration], jsii.get(self, "executeCommandConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsClusterConfiguration]:
        return typing.cast(typing.Optional[EcsClusterConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EcsClusterConfiguration]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterDefaultCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class EcsClusterDefaultCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#capacity_provider EcsCluster#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#base EcsCluster#base}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#weight EcsCluster#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterDefaultCapacityProviderStrategy.__init__)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#capacity_provider EcsCluster#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#base EcsCluster#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#weight EcsCluster#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterDefaultCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsClusterDefaultCapacityProviderStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterDefaultCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(EcsClusterDefaultCapacityProviderStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsClusterDefaultCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterDefaultCapacityProviderStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsClusterDefaultCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterDefaultCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterDefaultCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterDefaultCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsClusterDefaultCapacityProviderStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterDefaultCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterDefaultCapacityProviderStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyOutputReference, "base").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyOutputReference, "capacity_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsClusterDefaultCapacityProviderStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsClusterDefaultCapacityProviderStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsClusterDefaultCapacityProviderStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterDefaultCapacityProviderStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterSetting",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class EcsClusterSetting:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#name EcsCluster#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#value EcsCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterSetting.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#name EcsCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_cluster#value EcsCluster#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsClusterSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsClusterSettingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterSettingList",
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
            type_hints = typing.get_type_hints(EcsClusterSettingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsClusterSettingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsClusterSettingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsClusterSettingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterSetting]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterSetting]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsClusterSetting]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsClusterSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsClusterSettingOutputReference",
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
            type_hints = typing.get_type_hints(EcsClusterSettingOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsClusterSetting, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsClusterSetting, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsClusterSetting, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsClusterSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_service aws_ecs_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_service aws_ecs_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsServiceConfig(
            name=name,
            capacity_provider_strategy=capacity_provider_strategy,
            cluster=cluster,
            deployment_circuit_breaker=deployment_circuit_breaker,
            deployment_controller=deployment_controller,
            deployment_maximum_percent=deployment_maximum_percent,
            deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
            desired_count=desired_count,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            force_new_deployment=force_new_deployment,
            health_check_grace_period_seconds=health_check_grace_period_seconds,
            iam_role=iam_role,
            id=id,
            launch_type=launch_type,
            load_balancer=load_balancer,
            network_configuration=network_configuration,
            ordered_placement_strategy=ordered_placement_strategy,
            placement_constraints=placement_constraints,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            scheduling_strategy=scheduling_strategy,
            service_registries=service_registries,
            tags=tags,
            tags_all=tags_all,
            task_definition=task_definition,
            timeouts=timeouts,
            wait_for_steady_state=wait_for_steady_state,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsService.put_capacity_provider_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putDeploymentCircuitBreaker")
    def put_deployment_circuit_breaker(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
        rollback: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.
        '''
        value = EcsServiceDeploymentCircuitBreaker(enable=enable, rollback=rollback)

        return typing.cast(None, jsii.invoke(self, "putDeploymentCircuitBreaker", [value]))

    @jsii.member(jsii_name="putDeploymentController")
    def put_deployment_controller(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        '''
        value = EcsServiceDeploymentController(type=type)

        return typing.cast(None, jsii.invoke(self, "putDeploymentController", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsService.put_load_balancer)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.
        '''
        value = EcsServiceNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putOrderedPlacementStrategy")
    def put_ordered_placement_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsService.put_ordered_placement_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrderedPlacementStrategy", [value]))

    @jsii.member(jsii_name="putPlacementConstraints")
    def put_placement_constraints(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsService.put_placement_constraints)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraints", [value]))

    @jsii.member(jsii_name="putServiceRegistries")
    def put_service_registries(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.
        '''
        value = EcsServiceServiceRegistries(
            registry_arn=registry_arn,
            container_name=container_name,
            container_port=container_port,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRegistries", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.
        '''
        value = EcsServiceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetDeploymentCircuitBreaker")
    def reset_deployment_circuit_breaker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentCircuitBreaker", []))

    @jsii.member(jsii_name="resetDeploymentController")
    def reset_deployment_controller(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentController", []))

    @jsii.member(jsii_name="resetDeploymentMaximumPercent")
    def reset_deployment_maximum_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMaximumPercent", []))

    @jsii.member(jsii_name="resetDeploymentMinimumHealthyPercent")
    def reset_deployment_minimum_healthy_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMinimumHealthyPercent", []))

    @jsii.member(jsii_name="resetDesiredCount")
    def reset_desired_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCount", []))

    @jsii.member(jsii_name="resetEnableEcsManagedTags")
    def reset_enable_ecs_managed_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEcsManagedTags", []))

    @jsii.member(jsii_name="resetEnableExecuteCommand")
    def reset_enable_execute_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExecuteCommand", []))

    @jsii.member(jsii_name="resetForceNewDeployment")
    def reset_force_new_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceNewDeployment", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriodSeconds")
    def reset_health_check_grace_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriodSeconds", []))

    @jsii.member(jsii_name="resetIamRole")
    def reset_iam_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRole", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetOrderedPlacementStrategy")
    def reset_ordered_placement_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderedPlacementStrategy", []))

    @jsii.member(jsii_name="resetPlacementConstraints")
    def reset_placement_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraints", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetSchedulingStrategy")
    def reset_scheduling_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingStrategy", []))

    @jsii.member(jsii_name="resetServiceRegistries")
    def reset_service_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistries", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTaskDefinition")
    def reset_task_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskDefinition", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWaitForSteadyState")
    def reset_wait_for_steady_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForSteadyState", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> "EcsServiceCapacityProviderStrategyList":
        return typing.cast("EcsServiceCapacityProviderStrategyList", jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(
        self,
    ) -> "EcsServiceDeploymentCircuitBreakerOutputReference":
        return typing.cast("EcsServiceDeploymentCircuitBreakerOutputReference", jsii.get(self, "deploymentCircuitBreaker"))

    @builtins.property
    @jsii.member(jsii_name="deploymentController")
    def deployment_controller(self) -> "EcsServiceDeploymentControllerOutputReference":
        return typing.cast("EcsServiceDeploymentControllerOutputReference", jsii.get(self, "deploymentController"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "EcsServiceLoadBalancerList":
        return typing.cast("EcsServiceLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "EcsServiceNetworkConfigurationOutputReference":
        return typing.cast("EcsServiceNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategy")
    def ordered_placement_strategy(self) -> "EcsServiceOrderedPlacementStrategyList":
        return typing.cast("EcsServiceOrderedPlacementStrategyList", jsii.get(self, "orderedPlacementStrategy"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraints")
    def placement_constraints(self) -> "EcsServicePlacementConstraintsList":
        return typing.cast("EcsServicePlacementConstraintsList", jsii.get(self, "placementConstraints"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistries")
    def service_registries(self) -> "EcsServiceServiceRegistriesOutputReference":
        return typing.cast("EcsServiceServiceRegistriesOutputReference", jsii.get(self, "serviceRegistries"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EcsServiceTimeoutsOutputReference":
        return typing.cast("EcsServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreakerInput")
    def deployment_circuit_breaker_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], jsii.get(self, "deploymentCircuitBreakerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentControllerInput")
    def deployment_controller_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], jsii.get(self, "deploymentControllerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercentInput")
    def deployment_maximum_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMaximumPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercentInput")
    def deployment_minimum_healthy_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMinimumHealthyPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCountInput")
    def desired_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCountInput"))

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
    @jsii.member(jsii_name="forceNewDeploymentInput")
    def force_new_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceNewDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSecondsInput")
    def health_check_grace_period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleInput")
    def iam_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategyInput")
    def ordered_placement_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], jsii.get(self, "orderedPlacementStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintsInput")
    def placement_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]], jsii.get(self, "placementConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategyInput")
    def scheduling_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistriesInput")
    def service_registries_input(
        self,
    ) -> typing.Optional["EcsServiceServiceRegistries"]:
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], jsii.get(self, "serviceRegistriesInput"))

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
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EcsServiceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EcsServiceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyStateInput")
    def wait_for_steady_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForSteadyStateInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMaximumPercent"))

    @deployment_maximum_percent.setter
    def deployment_maximum_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "deployment_maximum_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMaximumPercent", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMinimumHealthyPercent"))

    @deployment_minimum_healthy_percent.setter
    def deployment_minimum_healthy_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "deployment_minimum_healthy_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMinimumHealthyPercent", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCount"))

    @desired_count.setter
    def desired_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "desired_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCount", value)

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
            type_hints = typing.get_type_hints(getattr(EcsService, "enable_ecs_managed_tags").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsService, "enable_execute_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExecuteCommand", value)

    @builtins.property
    @jsii.member(jsii_name="forceNewDeployment")
    def force_new_deployment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceNewDeployment"))

    @force_new_deployment.setter
    def force_new_deployment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "force_new_deployment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceNewDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriodSeconds"))

    @health_check_grace_period_seconds.setter
    def health_check_grace_period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "health_check_grace_period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "iam_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "launch_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "platform_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "propagate_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategy")
    def scheduling_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingStrategy"))

    @scheduling_strategy.setter
    def scheduling_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "scheduling_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "task_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyState")
    def wait_for_steady_state(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForSteadyState"))

    @wait_for_steady_state.setter
    def wait_for_steady_state(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsService, "wait_for_steady_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSteadyState", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class EcsServiceCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider EcsService#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#base EcsService#base}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#weight EcsService#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceCapacityProviderStrategy.__init__)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider EcsService#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#base EcsService#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#weight EcsService#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceCapacityProviderStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(EcsServiceCapacityProviderStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceCapacityProviderStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceCapacityProviderStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceCapacityProviderStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyOutputReference, "base").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyOutputReference, "capacity_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceCapacityProviderStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceConfig",
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
        "capacity_provider_strategy": "capacityProviderStrategy",
        "cluster": "cluster",
        "deployment_circuit_breaker": "deploymentCircuitBreaker",
        "deployment_controller": "deploymentController",
        "deployment_maximum_percent": "deploymentMaximumPercent",
        "deployment_minimum_healthy_percent": "deploymentMinimumHealthyPercent",
        "desired_count": "desiredCount",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "force_new_deployment": "forceNewDeployment",
        "health_check_grace_period_seconds": "healthCheckGracePeriodSeconds",
        "iam_role": "iamRole",
        "id": "id",
        "launch_type": "launchType",
        "load_balancer": "loadBalancer",
        "network_configuration": "networkConfiguration",
        "ordered_placement_strategy": "orderedPlacementStrategy",
        "placement_constraints": "placementConstraints",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "scheduling_strategy": "schedulingStrategy",
        "service_registries": "serviceRegistries",
        "tags": "tags",
        "tags_all": "tagsAll",
        "task_definition": "taskDefinition",
        "timeouts": "timeouts",
        "wait_for_steady_state": "waitForSteadyState",
    },
)
class EcsServiceConfig(cdktf.TerraformMetaArguments):
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
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment_circuit_breaker, dict):
            deployment_circuit_breaker = EcsServiceDeploymentCircuitBreaker(**deployment_circuit_breaker)
        if isinstance(deployment_controller, dict):
            deployment_controller = EcsServiceDeploymentController(**deployment_controller)
        if isinstance(network_configuration, dict):
            network_configuration = EcsServiceNetworkConfiguration(**network_configuration)
        if isinstance(service_registries, dict):
            service_registries = EcsServiceServiceRegistries(**service_registries)
        if isinstance(timeouts, dict):
            timeouts = EcsServiceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument deployment_circuit_breaker", value=deployment_circuit_breaker, expected_type=type_hints["deployment_circuit_breaker"])
            check_type(argname="argument deployment_controller", value=deployment_controller, expected_type=type_hints["deployment_controller"])
            check_type(argname="argument deployment_maximum_percent", value=deployment_maximum_percent, expected_type=type_hints["deployment_maximum_percent"])
            check_type(argname="argument deployment_minimum_healthy_percent", value=deployment_minimum_healthy_percent, expected_type=type_hints["deployment_minimum_healthy_percent"])
            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument force_new_deployment", value=force_new_deployment, expected_type=type_hints["force_new_deployment"])
            check_type(argname="argument health_check_grace_period_seconds", value=health_check_grace_period_seconds, expected_type=type_hints["health_check_grace_period_seconds"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument ordered_placement_strategy", value=ordered_placement_strategy, expected_type=type_hints["ordered_placement_strategy"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument scheduling_strategy", value=scheduling_strategy, expected_type=type_hints["scheduling_strategy"])
            check_type(argname="argument service_registries", value=service_registries, expected_type=type_hints["service_registries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait_for_steady_state", value=wait_for_steady_state, expected_type=type_hints["wait_for_steady_state"])
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
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            self._values["cluster"] = cluster
        if deployment_circuit_breaker is not None:
            self._values["deployment_circuit_breaker"] = deployment_circuit_breaker
        if deployment_controller is not None:
            self._values["deployment_controller"] = deployment_controller
        if deployment_maximum_percent is not None:
            self._values["deployment_maximum_percent"] = deployment_maximum_percent
        if deployment_minimum_healthy_percent is not None:
            self._values["deployment_minimum_healthy_percent"] = deployment_minimum_healthy_percent
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if force_new_deployment is not None:
            self._values["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            self._values["health_check_grace_period_seconds"] = health_check_grace_period_seconds
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if id is not None:
            self._values["id"] = id
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if ordered_placement_strategy is not None:
            self._values["ordered_placement_strategy"] = ordered_placement_strategy
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if scheduling_strategy is not None:
            self._values["scheduling_strategy"] = scheduling_strategy
        if service_registries is not None:
            self._values["service_registries"] = service_registries
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if task_definition is not None:
            self._values["task_definition"] = task_definition
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if wait_for_steady_state is not None:
            self._values["wait_for_steady_state"] = wait_for_steady_state

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], result)

    @builtins.property
    def cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.'''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_circuit_breaker(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        '''deployment_circuit_breaker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        '''
        result = self._values.get("deployment_circuit_breaker")
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], result)

    @builtins.property
    def deployment_controller(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        '''deployment_controller block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        '''
        result = self._values.get("deployment_controller")
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], result)

    @builtins.property
    def deployment_maximum_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.'''
        result = self._values.get("deployment_maximum_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deployment_minimum_healthy_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.'''
        result = self._values.get("deployment_minimum_healthy_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.'''
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.'''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_execute_command(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.'''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_new_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.'''
        result = self._values.get("force_new_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check_grace_period_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.'''
        result = self._values.get("health_check_grace_period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.'''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], result)

    @builtins.property
    def ordered_placement_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        '''ordered_placement_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        '''
        result = self._values.get("ordered_placement_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        '''placement_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.'''
        result = self._values.get("scheduling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_registries(self) -> typing.Optional["EcsServiceServiceRegistries"]:
        '''service_registries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        '''
        result = self._values.get("service_registries")
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.'''
        result = self._values.get("task_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EcsServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EcsServiceTimeouts"], result)

    @builtins.property
    def wait_for_steady_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.'''
        result = self._values.get("wait_for_steady_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceDeploymentCircuitBreaker",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable", "rollback": "rollback"},
)
class EcsServiceDeploymentCircuitBreaker:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
        rollback: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceDeploymentCircuitBreaker.__init__)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument rollback", value=rollback, expected_type=type_hints["rollback"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
            "rollback": rollback,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def rollback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.'''
        result = self._values.get("rollback")
        assert result is not None, "Required property 'rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentCircuitBreaker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentCircuitBreakerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceDeploymentCircuitBreakerOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceDeploymentCircuitBreakerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackInput")
    def rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rollbackInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceDeploymentCircuitBreakerOutputReference, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="rollback")
    def rollback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rollback"))

    @rollback.setter
    def rollback(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceDeploymentCircuitBreakerOutputReference, "rollback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollback", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentCircuitBreaker]:
        return typing.cast(typing.Optional[EcsServiceDeploymentCircuitBreaker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentCircuitBreaker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceDeploymentCircuitBreakerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceDeploymentController",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class EcsServiceDeploymentController:
    def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceDeploymentController.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentController(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentControllerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceDeploymentControllerOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceDeploymentControllerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

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
            type_hints = typing.get_type_hints(getattr(EcsServiceDeploymentControllerOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentController]:
        return typing.cast(typing.Optional[EcsServiceDeploymentController], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentController],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceDeploymentControllerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "elb_name": "elbName",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsServiceLoadBalancer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: jsii.Number,
        elb_name: typing.Optional[builtins.str] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param elb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#elb_name EcsService#elb_name}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#target_group_arn EcsService#target_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceLoadBalancer.__init__)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument elb_name", value=elb_name, expected_type=type_hints["elb_name"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
            "container_port": container_port,
        }
        if elb_name is not None:
            self._values["elb_name"] = elb_name
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        assert result is not None, "Required property 'container_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def elb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#elb_name EcsService#elb_name}.'''
        result = self._values.get("elb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#target_group_arn EcsService#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceLoadBalancerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceLoadBalancerList",
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
            type_hints = typing.get_type_hints(EcsServiceLoadBalancerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsServiceLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceLoadBalancerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceLoadBalancerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceLoadBalancerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetElbName")
    def reset_elb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElbName", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="elbNameInput")
    def elb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerOutputReference, "container_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="elbName")
    def elb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elbName"))

    @elb_name.setter
    def elb_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerOutputReference, "elb_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elbName", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerOutputReference, "target_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceLoadBalancerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class EcsServiceNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceNetworkConfiguration.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceNetworkConfigurationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceNetworkConfigurationOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceNetworkConfigurationOutputReference, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceNetworkConfigurationOutputReference, "subnets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceNetworkConfiguration]:
        return typing.cast(typing.Optional[EcsServiceNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceOrderedPlacementStrategy",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "field": "field"},
)
class EcsServiceOrderedPlacementStrategy:
    def __init__(
        self,
        *,
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#field EcsService#field}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceOrderedPlacementStrategy.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#field EcsService#field}.'''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceOrderedPlacementStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceOrderedPlacementStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceOrderedPlacementStrategyList",
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
            type_hints = typing.get_type_hints(EcsServiceOrderedPlacementStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceOrderedPlacementStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceOrderedPlacementStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceOrderedPlacementStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceOrderedPlacementStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceOrderedPlacementStrategyOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceOrderedPlacementStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceOrderedPlacementStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServicePlacementConstraints",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class EcsServicePlacementConstraints:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#expression EcsService#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServicePlacementConstraints.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#expression EcsService#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServicePlacementConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServicePlacementConstraintsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServicePlacementConstraintsList",
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
            type_hints = typing.get_type_hints(EcsServicePlacementConstraintsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServicePlacementConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServicePlacementConstraintsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServicePlacementConstraintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServicePlacementConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServicePlacementConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(EcsServicePlacementConstraintsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServicePlacementConstraintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceServiceRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "registry_arn": "registryArn",
        "container_name": "containerName",
        "container_port": "containerPort",
        "port": "port",
    },
)
class EcsServiceServiceRegistries:
    def __init__(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceServiceRegistries.__init__)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_arn": registry_arn,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceRegistriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceServiceRegistriesOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceServiceRegistriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="registryArnInput")
    def registry_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceServiceRegistriesOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceServiceRegistriesOutputReference, "container_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceServiceRegistriesOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="registryArn")
    def registry_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryArn"))

    @registry_arn.setter
    def registry_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceServiceRegistriesOutputReference, "registry_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceServiceRegistries]:
        return typing.cast(typing.Optional[EcsServiceServiceRegistries], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceRegistries],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceServiceRegistriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class EcsServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsServiceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsServiceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EcsServiceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EcsServiceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsServiceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTag(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTag",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag aws_ecs_tag}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        key: builtins.str,
        resource_arn: builtins.str,
        value: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag aws_ecs_tag} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#key EcsTag#key}.
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#resource_arn EcsTag#resource_arn}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#value EcsTag#value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#id EcsTag#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTag.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsTagConfig(
            key=key,
            resource_arn=resource_arn,
            value=value,
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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTag, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTag, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTag, "resource_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTag, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTagConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key": "key",
        "resource_arn": "resourceArn",
        "value": "value",
        "id": "id",
    },
)
class EcsTagConfig(cdktf.TerraformMetaArguments):
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
        key: builtins.str,
        resource_arn: builtins.str,
        value: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#key EcsTag#key}.
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#resource_arn EcsTag#resource_arn}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#value EcsTag#value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#id EcsTag#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTagConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "resource_arn": resource_arn,
            "value": value,
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
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#key EcsTag#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#resource_arn EcsTag#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#value EcsTag#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_tag#id EcsTag#id}.

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
        return "EcsTagConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition aws_ecs_task_definition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_definitions: builtins.str,
        family: builtins.str,
        cpu: typing.Optional[builtins.str] = None,
        ephemeral_storage: typing.Optional[typing.Union["EcsTaskDefinitionEphemeralStorage", typing.Dict[str, typing.Any]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inference_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
        network_mode: typing.Optional[builtins.str] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        proxy_configuration: typing.Optional[typing.Union["EcsTaskDefinitionProxyConfiguration", typing.Dict[str, typing.Any]]] = None,
        requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_platform: typing.Optional[typing.Union["EcsTaskDefinitionRuntimePlatform", typing.Dict[str, typing.Any]]] = None,
        skip_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_role_arn: typing.Optional[builtins.str] = None,
        volume: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition aws_ecs_task_definition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inference_accelerator: inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        :param ipc_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.
        :param pid_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        :param requires_compatibilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.
        :param runtime_platform: runtime_platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        :param skip_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.
        :param task_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsTaskDefinitionConfig(
            container_definitions=container_definitions,
            family=family,
            cpu=cpu,
            ephemeral_storage=ephemeral_storage,
            execution_role_arn=execution_role_arn,
            id=id,
            inference_accelerator=inference_accelerator,
            ipc_mode=ipc_mode,
            memory=memory,
            network_mode=network_mode,
            pid_mode=pid_mode,
            placement_constraints=placement_constraints,
            proxy_configuration=proxy_configuration,
            requires_compatibilities=requires_compatibilities,
            runtime_platform=runtime_platform,
            skip_destroy=skip_destroy,
            tags=tags,
            tags_all=tags_all,
            task_role_arn=task_role_arn,
            volume=volume,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEphemeralStorage")
    def put_ephemeral_storage(self, *, size_in_gib: jsii.Number) -> None:
        '''
        :param size_in_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.
        '''
        value = EcsTaskDefinitionEphemeralStorage(size_in_gib=size_in_gib)

        return typing.cast(None, jsii.invoke(self, "putEphemeralStorage", [value]))

    @jsii.member(jsii_name="putInferenceAccelerator")
    def put_inference_accelerator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinition.put_inference_accelerator)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInferenceAccelerator", [value]))

    @jsii.member(jsii_name="putPlacementConstraints")
    def put_placement_constraints(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinition.put_placement_constraints)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraints", [value]))

    @jsii.member(jsii_name="putProxyConfiguration")
    def put_proxy_configuration(
        self,
        *,
        container_name: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        '''
        value = EcsTaskDefinitionProxyConfiguration(
            container_name=container_name, properties=properties, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putProxyConfiguration", [value]))

    @jsii.member(jsii_name="putRuntimePlatform")
    def put_runtime_platform(
        self,
        *,
        cpu_architecture: typing.Optional[builtins.str] = None,
        operating_system_family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.
        :param operating_system_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.
        '''
        value = EcsTaskDefinitionRuntimePlatform(
            cpu_architecture=cpu_architecture,
            operating_system_family=operating_system_family,
        )

        return typing.cast(None, jsii.invoke(self, "putRuntimePlatform", [value]))

    @jsii.member(jsii_name="putVolume")
    def put_volume(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinition.put_volume)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolume", [value]))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetEphemeralStorage")
    def reset_ephemeral_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralStorage", []))

    @jsii.member(jsii_name="resetExecutionRoleArn")
    def reset_execution_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInferenceAccelerator")
    def reset_inference_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInferenceAccelerator", []))

    @jsii.member(jsii_name="resetIpcMode")
    def reset_ipc_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpcMode", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetPidMode")
    def reset_pid_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPidMode", []))

    @jsii.member(jsii_name="resetPlacementConstraints")
    def reset_placement_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraints", []))

    @jsii.member(jsii_name="resetProxyConfiguration")
    def reset_proxy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyConfiguration", []))

    @jsii.member(jsii_name="resetRequiresCompatibilities")
    def reset_requires_compatibilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiresCompatibilities", []))

    @jsii.member(jsii_name="resetRuntimePlatform")
    def reset_runtime_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimePlatform", []))

    @jsii.member(jsii_name="resetSkipDestroy")
    def reset_skip_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipDestroy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTaskRoleArn")
    def reset_task_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskRoleArn", []))

    @jsii.member(jsii_name="resetVolume")
    def reset_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolume", []))

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
    @jsii.member(jsii_name="ephemeralStorage")
    def ephemeral_storage(self) -> "EcsTaskDefinitionEphemeralStorageOutputReference":
        return typing.cast("EcsTaskDefinitionEphemeralStorageOutputReference", jsii.get(self, "ephemeralStorage"))

    @builtins.property
    @jsii.member(jsii_name="inferenceAccelerator")
    def inference_accelerator(self) -> "EcsTaskDefinitionInferenceAcceleratorList":
        return typing.cast("EcsTaskDefinitionInferenceAcceleratorList", jsii.get(self, "inferenceAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraints")
    def placement_constraints(self) -> "EcsTaskDefinitionPlacementConstraintsList":
        return typing.cast("EcsTaskDefinitionPlacementConstraintsList", jsii.get(self, "placementConstraints"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> "EcsTaskDefinitionProxyConfigurationOutputReference":
        return typing.cast("EcsTaskDefinitionProxyConfigurationOutputReference", jsii.get(self, "proxyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @builtins.property
    @jsii.member(jsii_name="runtimePlatform")
    def runtime_platform(self) -> "EcsTaskDefinitionRuntimePlatformOutputReference":
        return typing.cast("EcsTaskDefinitionRuntimePlatformOutputReference", jsii.get(self, "runtimePlatform"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> "EcsTaskDefinitionVolumeList":
        return typing.cast("EcsTaskDefinitionVolumeList", jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="containerDefinitionsInput")
    def container_definitions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerDefinitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorageInput")
    def ephemeral_storage_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionEphemeralStorage"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionEphemeralStorage"], jsii.get(self, "ephemeralStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inferenceAcceleratorInput")
    def inference_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]], jsii.get(self, "inferenceAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="ipcModeInput")
    def ipc_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipcModeInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="pidModeInput")
    def pid_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pidModeInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintsInput")
    def placement_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]], jsii.get(self, "placementConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfigurationInput")
    def proxy_configuration_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionProxyConfiguration"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionProxyConfiguration"], jsii.get(self, "proxyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requiresCompatibilitiesInput")
    def requires_compatibilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiresCompatibilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimePlatformInput")
    def runtime_platform_input(
        self,
    ) -> typing.Optional["EcsTaskDefinitionRuntimePlatform"]:
        return typing.cast(typing.Optional["EcsTaskDefinitionRuntimePlatform"], jsii.get(self, "runtimePlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="skipDestroyInput")
    def skip_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipDestroyInput"))

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
    @jsii.member(jsii_name="taskRoleArnInput")
    def task_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionVolume"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionVolume"]]], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerDefinitions")
    def container_definitions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerDefinitions"))

    @container_definitions.setter
    def container_definitions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "container_definitions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerDefinitions", value)

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "execution_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipcMode")
    def ipc_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipcMode"))

    @ipc_mode.setter
    def ipc_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "ipc_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipcMode", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "network_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value)

    @builtins.property
    @jsii.member(jsii_name="pidMode")
    def pid_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pidMode"))

    @pid_mode.setter
    def pid_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "pid_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pidMode", value)

    @builtins.property
    @jsii.member(jsii_name="requiresCompatibilities")
    def requires_compatibilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiresCompatibilities"))

    @requires_compatibilities.setter
    def requires_compatibilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "requires_compatibilities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiresCompatibilities", value)

    @builtins.property
    @jsii.member(jsii_name="skipDestroy")
    def skip_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipDestroy"))

    @skip_destroy.setter
    def skip_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "skip_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="taskRoleArn")
    def task_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskRoleArn"))

    @task_role_arn.setter
    def task_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinition, "task_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskRoleArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_definitions": "containerDefinitions",
        "family": "family",
        "cpu": "cpu",
        "ephemeral_storage": "ephemeralStorage",
        "execution_role_arn": "executionRoleArn",
        "id": "id",
        "inference_accelerator": "inferenceAccelerator",
        "ipc_mode": "ipcMode",
        "memory": "memory",
        "network_mode": "networkMode",
        "pid_mode": "pidMode",
        "placement_constraints": "placementConstraints",
        "proxy_configuration": "proxyConfiguration",
        "requires_compatibilities": "requiresCompatibilities",
        "runtime_platform": "runtimePlatform",
        "skip_destroy": "skipDestroy",
        "tags": "tags",
        "tags_all": "tagsAll",
        "task_role_arn": "taskRoleArn",
        "volume": "volume",
    },
)
class EcsTaskDefinitionConfig(cdktf.TerraformMetaArguments):
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
        container_definitions: builtins.str,
        family: builtins.str,
        cpu: typing.Optional[builtins.str] = None,
        ephemeral_storage: typing.Optional[typing.Union["EcsTaskDefinitionEphemeralStorage", typing.Dict[str, typing.Any]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inference_accelerator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionInferenceAccelerator", typing.Dict[str, typing.Any]]]]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
        network_mode: typing.Optional[builtins.str] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionPlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        proxy_configuration: typing.Optional[typing.Union["EcsTaskDefinitionProxyConfiguration", typing.Dict[str, typing.Any]]] = None,
        requires_compatibilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_platform: typing.Optional[typing.Union["EcsTaskDefinitionRuntimePlatform", typing.Dict[str, typing.Any]]] = None,
        skip_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_role_arn: typing.Optional[builtins.str] = None,
        volume: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskDefinitionVolume", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_definitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.
        :param family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inference_accelerator: inference_accelerator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        :param ipc_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.
        :param network_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.
        :param pid_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        :param requires_compatibilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.
        :param runtime_platform: runtime_platform block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        :param skip_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.
        :param task_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ephemeral_storage, dict):
            ephemeral_storage = EcsTaskDefinitionEphemeralStorage(**ephemeral_storage)
        if isinstance(proxy_configuration, dict):
            proxy_configuration = EcsTaskDefinitionProxyConfiguration(**proxy_configuration)
        if isinstance(runtime_platform, dict):
            runtime_platform = EcsTaskDefinitionRuntimePlatform(**runtime_platform)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_definitions", value=container_definitions, expected_type=type_hints["container_definitions"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inference_accelerator", value=inference_accelerator, expected_type=type_hints["inference_accelerator"])
            check_type(argname="argument ipc_mode", value=ipc_mode, expected_type=type_hints["ipc_mode"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument pid_mode", value=pid_mode, expected_type=type_hints["pid_mode"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
            check_type(argname="argument requires_compatibilities", value=requires_compatibilities, expected_type=type_hints["requires_compatibilities"])
            check_type(argname="argument runtime_platform", value=runtime_platform, expected_type=type_hints["runtime_platform"])
            check_type(argname="argument skip_destroy", value=skip_destroy, expected_type=type_hints["skip_destroy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument task_role_arn", value=task_role_arn, expected_type=type_hints["task_role_arn"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_definitions": container_definitions,
            "family": family,
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
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage is not None:
            self._values["ephemeral_storage"] = ephemeral_storage
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if id is not None:
            self._values["id"] = id
        if inference_accelerator is not None:
            self._values["inference_accelerator"] = inference_accelerator
        if ipc_mode is not None:
            self._values["ipc_mode"] = ipc_mode
        if memory is not None:
            self._values["memory"] = memory
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if pid_mode is not None:
            self._values["pid_mode"] = pid_mode
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if proxy_configuration is not None:
            self._values["proxy_configuration"] = proxy_configuration
        if requires_compatibilities is not None:
            self._values["requires_compatibilities"] = requires_compatibilities
        if runtime_platform is not None:
            self._values["runtime_platform"] = runtime_platform
        if skip_destroy is not None:
            self._values["skip_destroy"] = skip_destroy
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if task_role_arn is not None:
            self._values["task_role_arn"] = task_role_arn
        if volume is not None:
            self._values["volume"] = volume

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
    def container_definitions(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_definitions EcsTaskDefinition#container_definitions}.'''
        result = self._values.get("container_definitions")
        assert result is not None, "Required property 'container_definitions' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#family EcsTaskDefinition#family}.'''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu EcsTaskDefinition#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_storage(self) -> typing.Optional["EcsTaskDefinitionEphemeralStorage"]:
        '''ephemeral_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ephemeral_storage EcsTaskDefinition#ephemeral_storage}
        '''
        result = self._values.get("ephemeral_storage")
        return typing.cast(typing.Optional["EcsTaskDefinitionEphemeralStorage"], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#execution_role_arn EcsTaskDefinition#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#id EcsTaskDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inference_accelerator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]]:
        '''inference_accelerator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#inference_accelerator EcsTaskDefinition#inference_accelerator}
        '''
        result = self._values.get("inference_accelerator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionInferenceAccelerator"]]], result)

    @builtins.property
    def ipc_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#ipc_mode EcsTaskDefinition#ipc_mode}.'''
        result = self._values.get("ipc_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#memory EcsTaskDefinition#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#network_mode EcsTaskDefinition#network_mode}.'''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pid_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#pid_mode EcsTaskDefinition#pid_mode}.'''
        result = self._values.get("pid_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]]:
        '''placement_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#placement_constraints EcsTaskDefinition#placement_constraints}
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionPlacementConstraints"]]], result)

    @builtins.property
    def proxy_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionProxyConfiguration"]:
        '''proxy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#proxy_configuration EcsTaskDefinition#proxy_configuration}
        '''
        result = self._values.get("proxy_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionProxyConfiguration"], result)

    @builtins.property
    def requires_compatibilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#requires_compatibilities EcsTaskDefinition#requires_compatibilities}.'''
        result = self._values.get("requires_compatibilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def runtime_platform(self) -> typing.Optional["EcsTaskDefinitionRuntimePlatform"]:
        '''runtime_platform block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#runtime_platform EcsTaskDefinition#runtime_platform}
        '''
        result = self._values.get("runtime_platform")
        return typing.cast(typing.Optional["EcsTaskDefinitionRuntimePlatform"], result)

    @builtins.property
    def skip_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#skip_destroy EcsTaskDefinition#skip_destroy}.'''
        result = self._values.get("skip_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags EcsTaskDefinition#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#tags_all EcsTaskDefinition#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#task_role_arn EcsTaskDefinition#task_role_arn}.'''
        result = self._values.get("task_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionVolume"]]]:
        '''volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#volume EcsTaskDefinition#volume}
        '''
        result = self._values.get("volume")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskDefinitionVolume"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionEphemeralStorage",
    jsii_struct_bases=[],
    name_mapping={"size_in_gib": "sizeInGib"},
)
class EcsTaskDefinitionEphemeralStorage:
    def __init__(self, *, size_in_gib: jsii.Number) -> None:
        '''
        :param size_in_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionEphemeralStorage.__init__)
            check_type(argname="argument size_in_gib", value=size_in_gib, expected_type=type_hints["size_in_gib"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_in_gib": size_in_gib,
        }

    @builtins.property
    def size_in_gib(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#size_in_gib EcsTaskDefinition#size_in_gib}.'''
        result = self._values.get("size_in_gib")
        assert result is not None, "Required property 'size_in_gib' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionEphemeralStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionEphemeralStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionEphemeralStorageOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionEphemeralStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sizeInGibInput")
    def size_in_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGibInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGib")
    def size_in_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGib"))

    @size_in_gib.setter
    def size_in_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionEphemeralStorageOutputReference, "size_in_gib").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGib", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionEphemeralStorage]:
        return typing.cast(typing.Optional[EcsTaskDefinitionEphemeralStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionEphemeralStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionEphemeralStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionInferenceAccelerator",
    jsii_struct_bases=[],
    name_mapping={"device_name": "deviceName", "device_type": "deviceType"},
)
class EcsTaskDefinitionInferenceAccelerator:
    def __init__(self, *, device_name: builtins.str, device_type: builtins.str) -> None:
        '''
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_name EcsTaskDefinition#device_name}.
        :param device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_type EcsTaskDefinition#device_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionInferenceAccelerator.__init__)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_name": device_name,
            "device_type": device_type,
        }

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_name EcsTaskDefinition#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#device_type EcsTaskDefinition#device_type}.'''
        result = self._values.get("device_type")
        assert result is not None, "Required property 'device_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionInferenceAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionInferenceAcceleratorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionInferenceAcceleratorList",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionInferenceAcceleratorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskDefinitionInferenceAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionInferenceAcceleratorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionInferenceAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionInferenceAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionInferenceAcceleratorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionInferenceAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionInferenceAcceleratorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeInput")
    def device_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorOutputReference, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="deviceType")
    def device_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceType"))

    @device_type.setter
    def device_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorOutputReference, "device_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionInferenceAccelerator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionInferenceAcceleratorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionPlacementConstraints",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class EcsTaskDefinitionPlacementConstraints:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#expression EcsTaskDefinition#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionPlacementConstraints.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#expression EcsTaskDefinition#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionPlacementConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionPlacementConstraintsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionPlacementConstraintsList",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionPlacementConstraintsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskDefinitionPlacementConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionPlacementConstraintsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionPlacementConstraintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionPlacementConstraints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionPlacementConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionPlacementConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionPlacementConstraintsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionPlacementConstraints, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionPlacementConstraintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionProxyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "properties": "properties",
        "type": "type",
    },
)
class EcsTaskDefinitionProxyConfiguration:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionProxyConfiguration.__init__)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
        }
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#container_name EcsTaskDefinition#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#properties EcsTaskDefinition#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#type EcsTaskDefinition#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionProxyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionProxyConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionProxyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionProxyConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionProxyConfigurationOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionProxyConfigurationOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionProxyConfigurationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionProxyConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionProxyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionProxyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionProxyConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionRuntimePlatform",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_architecture": "cpuArchitecture",
        "operating_system_family": "operatingSystemFamily",
    },
)
class EcsTaskDefinitionRuntimePlatform:
    def __init__(
        self,
        *,
        cpu_architecture: typing.Optional[builtins.str] = None,
        operating_system_family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.
        :param operating_system_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionRuntimePlatform.__init__)
            check_type(argname="argument cpu_architecture", value=cpu_architecture, expected_type=type_hints["cpu_architecture"])
            check_type(argname="argument operating_system_family", value=operating_system_family, expected_type=type_hints["operating_system_family"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_architecture is not None:
            self._values["cpu_architecture"] = cpu_architecture
        if operating_system_family is not None:
            self._values["operating_system_family"] = operating_system_family

    @builtins.property
    def cpu_architecture(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#cpu_architecture EcsTaskDefinition#cpu_architecture}.'''
        result = self._values.get("cpu_architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system_family(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#operating_system_family EcsTaskDefinition#operating_system_family}.'''
        result = self._values.get("operating_system_family")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionRuntimePlatform(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionRuntimePlatformOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionRuntimePlatformOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionRuntimePlatformOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuArchitecture")
    def reset_cpu_architecture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuArchitecture", []))

    @jsii.member(jsii_name="resetOperatingSystemFamily")
    def reset_operating_system_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystemFamily", []))

    @builtins.property
    @jsii.member(jsii_name="cpuArchitectureInput")
    def cpu_architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuArchitectureInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemFamilyInput")
    def operating_system_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuArchitecture")
    def cpu_architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuArchitecture"))

    @cpu_architecture.setter
    def cpu_architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionRuntimePlatformOutputReference, "cpu_architecture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuArchitecture", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystemFamily")
    def operating_system_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystemFamily"))

    @operating_system_family.setter
    def operating_system_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionRuntimePlatformOutputReference, "operating_system_family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystemFamily", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskDefinitionRuntimePlatform]:
        return typing.cast(typing.Optional[EcsTaskDefinitionRuntimePlatform], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionRuntimePlatform],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionRuntimePlatformOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolume",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "docker_volume_configuration": "dockerVolumeConfiguration",
        "efs_volume_configuration": "efsVolumeConfiguration",
        "fsx_windows_file_server_volume_configuration": "fsxWindowsFileServerVolumeConfiguration",
        "host_path": "hostPath",
    },
)
class EcsTaskDefinitionVolume:
    def __init__(
        self,
        *,
        name: builtins.str,
        docker_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeDockerVolumeConfiguration", typing.Dict[str, typing.Any]]] = None,
        efs_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeEfsVolumeConfiguration", typing.Dict[str, typing.Any]]] = None,
        fsx_windows_file_server_volume_configuration: typing.Optional[typing.Union["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration", typing.Dict[str, typing.Any]]] = None,
        host_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#name EcsTaskDefinition#name}.
        :param docker_volume_configuration: docker_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#docker_volume_configuration EcsTaskDefinition#docker_volume_configuration}
        :param efs_volume_configuration: efs_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#efs_volume_configuration EcsTaskDefinition#efs_volume_configuration}
        :param fsx_windows_file_server_volume_configuration: fsx_windows_file_server_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#fsx_windows_file_server_volume_configuration EcsTaskDefinition#fsx_windows_file_server_volume_configuration}
        :param host_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#host_path EcsTaskDefinition#host_path}.
        '''
        if isinstance(docker_volume_configuration, dict):
            docker_volume_configuration = EcsTaskDefinitionVolumeDockerVolumeConfiguration(**docker_volume_configuration)
        if isinstance(efs_volume_configuration, dict):
            efs_volume_configuration = EcsTaskDefinitionVolumeEfsVolumeConfiguration(**efs_volume_configuration)
        if isinstance(fsx_windows_file_server_volume_configuration, dict):
            fsx_windows_file_server_volume_configuration = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(**fsx_windows_file_server_volume_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolume.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument docker_volume_configuration", value=docker_volume_configuration, expected_type=type_hints["docker_volume_configuration"])
            check_type(argname="argument efs_volume_configuration", value=efs_volume_configuration, expected_type=type_hints["efs_volume_configuration"])
            check_type(argname="argument fsx_windows_file_server_volume_configuration", value=fsx_windows_file_server_volume_configuration, expected_type=type_hints["fsx_windows_file_server_volume_configuration"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if docker_volume_configuration is not None:
            self._values["docker_volume_configuration"] = docker_volume_configuration
        if efs_volume_configuration is not None:
            self._values["efs_volume_configuration"] = efs_volume_configuration
        if fsx_windows_file_server_volume_configuration is not None:
            self._values["fsx_windows_file_server_volume_configuration"] = fsx_windows_file_server_volume_configuration
        if host_path is not None:
            self._values["host_path"] = host_path

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#name EcsTaskDefinition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeDockerVolumeConfiguration"]:
        '''docker_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#docker_volume_configuration EcsTaskDefinition#docker_volume_configuration}
        '''
        result = self._values.get("docker_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeDockerVolumeConfiguration"], result)

    @builtins.property
    def efs_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfiguration"]:
        '''efs_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#efs_volume_configuration EcsTaskDefinition#efs_volume_configuration}
        '''
        result = self._values.get("efs_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfiguration"], result)

    @builtins.property
    def fsx_windows_file_server_volume_configuration(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration"]:
        '''fsx_windows_file_server_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#fsx_windows_file_server_volume_configuration EcsTaskDefinition#fsx_windows_file_server_volume_configuration}
        '''
        result = self._values.get("fsx_windows_file_server_volume_configuration")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration"], result)

    @builtins.property
    def host_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#host_path EcsTaskDefinition#host_path}.'''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeDockerVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "autoprovision": "autoprovision",
        "driver": "driver",
        "driver_opts": "driverOpts",
        "labels": "labels",
        "scope": "scope",
    },
)
class EcsTaskDefinitionVolumeDockerVolumeConfiguration:
    def __init__(
        self,
        *,
        autoprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.
        :param driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.
        :param driver_opts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeDockerVolumeConfiguration.__init__)
            check_type(argname="argument autoprovision", value=autoprovision, expected_type=type_hints["autoprovision"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument driver_opts", value=driver_opts, expected_type=type_hints["driver_opts"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoprovision is not None:
            self._values["autoprovision"] = autoprovision
        if driver is not None:
            self._values["driver"] = driver
        if driver_opts is not None:
            self._values["driver_opts"] = driver_opts
        if labels is not None:
            self._values["labels"] = labels
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def autoprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.'''
        result = self._values.get("autoprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def driver(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.'''
        result = self._values.get("driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_opts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.'''
        result = self._values.get("driver_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeDockerVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoprovision")
    def reset_autoprovision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoprovision", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetDriverOpts")
    def reset_driver_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverOpts", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="autoprovisionInput")
    def autoprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driverOptsInput")
    def driver_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoprovision")
    def autoprovision(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoprovision"))

    @autoprovision.setter
    def autoprovision(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "autoprovision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoprovision", value)

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="driverOpts")
    def driver_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverOpts"))

    @driver_opts.setter
    def driver_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "driver_opts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverOpts", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeEfsVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "authorization_config": "authorizationConfig",
        "root_directory": "rootDirectory",
        "transit_encryption": "transitEncryption",
        "transit_encryption_port": "transitEncryptionPort",
    },
)
class EcsTaskDefinitionVolumeEfsVolumeConfiguration:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        authorization_config: typing.Optional[typing.Union["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig", typing.Dict[str, typing.Any]]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        transit_encryption: typing.Optional[builtins.str] = None,
        transit_encryption_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        :param transit_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.
        :param transit_encryption_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.
        '''
        if isinstance(authorization_config, dict):
            authorization_config = EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeEfsVolumeConfiguration.__init__)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
            check_type(argname="argument transit_encryption", value=transit_encryption, expected_type=type_hints["transit_encryption"])
            check_type(argname="argument transit_encryption_port", value=transit_encryption_port, expected_type=type_hints["transit_encryption_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_system_id": file_system_id,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if root_directory is not None:
            self._values["root_directory"] = root_directory
        if transit_encryption is not None:
            self._values["transit_encryption"] = transit_encryption
        if transit_encryption_port is not None:
            self._values["transit_encryption_port"] = transit_encryption_port

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(
        self,
    ) -> typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig"]:
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional["EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig"], result)

    @builtins.property
    def root_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.'''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.'''
        result = self._values.get("transit_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_encryption_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.'''
        result = self._values.get("transit_encryption_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeEfsVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={"access_point_id": "accessPointId", "iam": "iam"},
)
class EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig:
    def __init__(
        self,
        *,
        access_point_id: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_point_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig.__init__)
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_point_id is not None:
            self._values["access_point_id"] = access_point_id
        if iam is not None:
            self._values["iam"] = iam

    @builtins.property
    def access_point_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.'''
        result = self._values.get("access_point_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.'''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessPointId")
    def reset_access_point_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPointId", []))

    @jsii.member(jsii_name="resetIam")
    def reset_iam(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIam", []))

    @builtins.property
    @jsii.member(jsii_name="accessPointIdInput")
    def access_point_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInput")
    def iam_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInput"))

    @builtins.property
    @jsii.member(jsii_name="accessPointId")
    def access_point_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPointId"))

    @access_point_id.setter
    def access_point_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference, "access_point_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPointId", value)

    @builtins.property
    @jsii.member(jsii_name="iam")
    def iam(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iam"))

    @iam.setter
    def iam(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference, "iam").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iam", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        access_point_id: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_point_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#access_point_id EcsTaskDefinition#access_point_id}.
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#iam EcsTaskDefinition#iam}.
        '''
        value = EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(
            access_point_id=access_point_id, iam=iam
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationConfig")
    def reset_authorization_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationConfig", []))

    @jsii.member(jsii_name="resetRootDirectory")
    def reset_root_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootDirectory", []))

    @jsii.member(jsii_name="resetTransitEncryption")
    def reset_transit_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryption", []))

    @jsii.member(jsii_name="resetTransitEncryptionPort")
    def reset_transit_encryption_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryptionPort", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionInput")
    def transit_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionPortInput")
    def transit_encryption_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "transitEncryptionPortInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, "file_system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, "root_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryption")
    def transit_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitEncryption"))

    @transit_encryption.setter
    def transit_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, "transit_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionPort")
    def transit_encryption_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "transitEncryptionPort"))

    @transit_encryption_port.setter
    def transit_encryption_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, "transit_encryption_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_config": "authorizationConfig",
        "file_system_id": "fileSystemId",
        "root_directory": "rootDirectory",
    },
)
class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration:
    def __init__(
        self,
        *,
        authorization_config: typing.Union["EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig", typing.Dict[str, typing.Any]],
        file_system_id: builtins.str,
        root_directory: builtins.str,
    ) -> None:
        '''
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        '''
        if isinstance(authorization_config, dict):
            authorization_config = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration.__init__)
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_config": authorization_config,
            "file_system_id": file_system_id,
            "root_directory": root_directory,
        }

    @builtins.property
    def authorization_config(
        self,
    ) -> "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig":
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        '''
        result = self._values.get("authorization_config")
        assert result is not None, "Required property 'authorization_config' is missing"
        return typing.cast("EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig", result)

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_directory(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.'''
        result = self._values.get("root_directory")
        assert result is not None, "Required property 'root_directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={"credentials_parameter": "credentialsParameter", "domain": "domain"},
)
class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig:
    def __init__(
        self,
        *,
        credentials_parameter: builtins.str,
        domain: builtins.str,
    ) -> None:
        '''
        :param credentials_parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig.__init__)
            check_type(argname="argument credentials_parameter", value=credentials_parameter, expected_type=type_hints["credentials_parameter"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "credentials_parameter": credentials_parameter,
            "domain": domain,
        }

    @builtins.property
    def credentials_parameter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.'''
        result = self._values.get("credentials_parameter")
        assert result is not None, "Required property 'credentials_parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="credentialsParameterInput")
    def credentials_parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsParameter")
    def credentials_parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsParameter"))

    @credentials_parameter.setter
    def credentials_parameter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference, "credentials_parameter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsParameter", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        credentials_parameter: builtins.str,
        domain: builtins.str,
    ) -> None:
        '''
        :param credentials_parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#credentials_parameter EcsTaskDefinition#credentials_parameter}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#domain EcsTaskDefinition#domain}.
        '''
        value = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(
            credentials_parameter=credentials_parameter, domain=domain
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootDirectoryInput")
    def root_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference, "file_system_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference, "root_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeList",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsTaskDefinitionVolumeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskDefinitionVolumeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionVolume]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionVolume]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskDefinitionVolume]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskDefinitionVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskDefinitionVolumeOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskDefinitionVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDockerVolumeConfiguration")
    def put_docker_volume_configuration(
        self,
        *,
        autoprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autoprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#autoprovision EcsTaskDefinition#autoprovision}.
        :param driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver EcsTaskDefinition#driver}.
        :param driver_opts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#driver_opts EcsTaskDefinition#driver_opts}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#labels EcsTaskDefinition#labels}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#scope EcsTaskDefinition#scope}.
        '''
        value = EcsTaskDefinitionVolumeDockerVolumeConfiguration(
            autoprovision=autoprovision,
            driver=driver,
            driver_opts=driver_opts,
            labels=labels,
            scope=scope,
        )

        return typing.cast(None, jsii.invoke(self, "putDockerVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putEfsVolumeConfiguration")
    def put_efs_volume_configuration(
        self,
        *,
        file_system_id: builtins.str,
        authorization_config: typing.Optional[typing.Union[EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig, typing.Dict[str, typing.Any]]] = None,
        root_directory: typing.Optional[builtins.str] = None,
        transit_encryption: typing.Optional[builtins.str] = None,
        transit_encryption_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        :param transit_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption EcsTaskDefinition#transit_encryption}.
        :param transit_encryption_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#transit_encryption_port EcsTaskDefinition#transit_encryption_port}.
        '''
        value = EcsTaskDefinitionVolumeEfsVolumeConfiguration(
            file_system_id=file_system_id,
            authorization_config=authorization_config,
            root_directory=root_directory,
            transit_encryption=transit_encryption,
            transit_encryption_port=transit_encryption_port,
        )

        return typing.cast(None, jsii.invoke(self, "putEfsVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putFsxWindowsFileServerVolumeConfiguration")
    def put_fsx_windows_file_server_volume_configuration(
        self,
        *,
        authorization_config: typing.Union[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig, typing.Dict[str, typing.Any]],
        file_system_id: builtins.str,
        root_directory: builtins.str,
    ) -> None:
        '''
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#authorization_config EcsTaskDefinition#authorization_config}
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#file_system_id EcsTaskDefinition#file_system_id}.
        :param root_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_definition#root_directory EcsTaskDefinition#root_directory}.
        '''
        value = EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(
            authorization_config=authorization_config,
            file_system_id=file_system_id,
            root_directory=root_directory,
        )

        return typing.cast(None, jsii.invoke(self, "putFsxWindowsFileServerVolumeConfiguration", [value]))

    @jsii.member(jsii_name="resetDockerVolumeConfiguration")
    def reset_docker_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerVolumeConfiguration", []))

    @jsii.member(jsii_name="resetEfsVolumeConfiguration")
    def reset_efs_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsVolumeConfiguration", []))

    @jsii.member(jsii_name="resetFsxWindowsFileServerVolumeConfiguration")
    def reset_fsx_windows_file_server_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsxWindowsFileServerVolumeConfiguration", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @builtins.property
    @jsii.member(jsii_name="dockerVolumeConfiguration")
    def docker_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference, jsii.get(self, "dockerVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="efsVolumeConfiguration")
    def efs_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference, jsii.get(self, "efsVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="fsxWindowsFileServerVolumeConfiguration")
    def fsx_windows_file_server_volume_configuration(
        self,
    ) -> EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference:
        return typing.cast(EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference, jsii.get(self, "fsxWindowsFileServerVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dockerVolumeConfigurationInput")
    def docker_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeDockerVolumeConfiguration], jsii.get(self, "dockerVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="efsVolumeConfigurationInput")
    def efs_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeEfsVolumeConfiguration], jsii.get(self, "efsVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fsxWindowsFileServerVolumeConfigurationInput")
    def fsx_windows_file_server_volume_configuration_input(
        self,
    ) -> typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration], jsii.get(self, "fsxWindowsFileServerVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeOutputReference, "host_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskDefinitionVolume, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskDefinitionVolume, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskDefinitionVolume, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskDefinitionVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set aws_ecs_task_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster: builtins.str,
        service: builtins.str,
        task_definition: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskSetCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsTaskSetNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        scale: typing.Optional[typing.Union["EcsTaskSetScale", typing.Dict[str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsTaskSetServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_until_stable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        wait_until_stable_timeout: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set aws_ecs_task_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.
        :param scale: scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.
        :param wait_until_stable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.
        :param wait_until_stable_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsTaskSetConfig(
            cluster=cluster,
            service=service,
            task_definition=task_definition,
            capacity_provider_strategy=capacity_provider_strategy,
            external_id=external_id,
            force_delete=force_delete,
            id=id,
            launch_type=launch_type,
            load_balancer=load_balancer,
            network_configuration=network_configuration,
            platform_version=platform_version,
            scale=scale,
            service_registries=service_registries,
            tags=tags,
            tags_all=tags_all,
            wait_until_stable=wait_until_stable,
            wait_until_stable_timeout=wait_until_stable_timeout,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskSetCapacityProviderStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSet.put_capacity_provider_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSet.put_load_balancer)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.
        '''
        value = EcsTaskSetNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putScale")
    def put_scale(
        self,
        *,
        unit: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.
        '''
        value_ = EcsTaskSetScale(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putScale", [value_]))

    @jsii.member(jsii_name="putServiceRegistries")
    def put_service_registries(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.
        '''
        value = EcsTaskSetServiceRegistries(
            registry_arn=registry_arn,
            container_name=container_name,
            container_port=container_port,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRegistries", [value]))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetScale")
    def reset_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScale", []))

    @jsii.member(jsii_name="resetServiceRegistries")
    def reset_service_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistries", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetWaitUntilStable")
    def reset_wait_until_stable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitUntilStable", []))

    @jsii.member(jsii_name="resetWaitUntilStableTimeout")
    def reset_wait_until_stable_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitUntilStableTimeout", []))

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
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> "EcsTaskSetCapacityProviderStrategyList":
        return typing.cast("EcsTaskSetCapacityProviderStrategyList", jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "EcsTaskSetLoadBalancerList":
        return typing.cast("EcsTaskSetLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "EcsTaskSetNetworkConfigurationOutputReference":
        return typing.cast("EcsTaskSetNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> "EcsTaskSetScaleOutputReference":
        return typing.cast("EcsTaskSetScaleOutputReference", jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistries")
    def service_registries(self) -> "EcsTaskSetServiceRegistriesOutputReference":
        return typing.cast("EcsTaskSetServiceRegistriesOutputReference", jsii.get(self, "serviceRegistries"))

    @builtins.property
    @jsii.member(jsii_name="stabilityStatus")
    def stability_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stabilityStatus"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="taskSetId")
    def task_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskSetId"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetCapacityProviderStrategy"]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EcsTaskSetNetworkConfiguration"]:
        return typing.cast(typing.Optional["EcsTaskSetNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInput")
    def scale_input(self) -> typing.Optional["EcsTaskSetScale"]:
        return typing.cast(typing.Optional["EcsTaskSetScale"], jsii.get(self, "scaleInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistriesInput")
    def service_registries_input(
        self,
    ) -> typing.Optional["EcsTaskSetServiceRegistries"]:
        return typing.cast(typing.Optional["EcsTaskSetServiceRegistries"], jsii.get(self, "serviceRegistriesInput"))

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
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableInput")
    def wait_until_stable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitUntilStableInput"))

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableTimeoutInput")
    def wait_until_stable_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitUntilStableTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "cluster").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "external_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "launch_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "platform_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "tags_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "task_definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="waitUntilStable")
    def wait_until_stable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitUntilStable"))

    @wait_until_stable.setter
    def wait_until_stable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "wait_until_stable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitUntilStable", value)

    @builtins.property
    @jsii.member(jsii_name="waitUntilStableTimeout")
    def wait_until_stable_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitUntilStableTimeout"))

    @wait_until_stable_timeout.setter
    def wait_until_stable_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSet, "wait_until_stable_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitUntilStableTimeout", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "weight": "weight",
        "base": "base",
    },
)
class EcsTaskSetCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        weight: jsii.Number,
        base: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider EcsTaskSet#capacity_provider}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#weight EcsTaskSet#weight}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#base EcsTaskSet#base}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetCapacityProviderStrategy.__init__)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity_provider": capacity_provider,
            "weight": weight,
        }
        if base is not None:
            self._values["base"] = base

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider EcsTaskSet#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#weight EcsTaskSet#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#base EcsTaskSet#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetCapacityProviderStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(EcsTaskSetCapacityProviderStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsTaskSetCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetCapacityProviderStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskSetCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskSetCapacityProviderStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskSetCapacityProviderStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyOutputReference, "base").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyOutputReference, "capacity_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskSetCapacityProviderStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetCapacityProviderStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster": "cluster",
        "service": "service",
        "task_definition": "taskDefinition",
        "capacity_provider_strategy": "capacityProviderStrategy",
        "external_id": "externalId",
        "force_delete": "forceDelete",
        "id": "id",
        "launch_type": "launchType",
        "load_balancer": "loadBalancer",
        "network_configuration": "networkConfiguration",
        "platform_version": "platformVersion",
        "scale": "scale",
        "service_registries": "serviceRegistries",
        "tags": "tags",
        "tags_all": "tagsAll",
        "wait_until_stable": "waitUntilStable",
        "wait_until_stable_timeout": "waitUntilStableTimeout",
    },
)
class EcsTaskSetConfig(cdktf.TerraformMetaArguments):
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
        cluster: builtins.str,
        service: builtins.str,
        task_definition: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsTaskSetCapacityProviderStrategy, typing.Dict[str, typing.Any]]]]] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsTaskSetLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsTaskSetNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        scale: typing.Optional[typing.Union["EcsTaskSetScale", typing.Dict[str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsTaskSetServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_until_stable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        wait_until_stable_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS EC2 Container Service.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.
        :param scale: scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.
        :param wait_until_stable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.
        :param wait_until_stable_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_configuration, dict):
            network_configuration = EcsTaskSetNetworkConfiguration(**network_configuration)
        if isinstance(scale, dict):
            scale = EcsTaskSetScale(**scale)
        if isinstance(service_registries, dict):
            service_registries = EcsTaskSetServiceRegistries(**service_registries)
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument scale", value=scale, expected_type=type_hints["scale"])
            check_type(argname="argument service_registries", value=service_registries, expected_type=type_hints["service_registries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument wait_until_stable", value=wait_until_stable, expected_type=type_hints["wait_until_stable"])
            check_type(argname="argument wait_until_stable_timeout", value=wait_until_stable_timeout, expected_type=type_hints["wait_until_stable_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "service": service,
            "task_definition": task_definition,
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
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if external_id is not None:
            self._values["external_id"] = external_id
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if id is not None:
            self._values["id"] = id
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if scale is not None:
            self._values["scale"] = scale
        if service_registries is not None:
            self._values["service_registries"] = service_registries
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if wait_until_stable is not None:
            self._values["wait_until_stable"] = wait_until_stable
        if wait_until_stable_timeout is not None:
            self._values["wait_until_stable_timeout"] = wait_until_stable_timeout

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
    def cluster(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#cluster EcsTaskSet#cluster}.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service EcsTaskSet#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#task_definition EcsTaskSet#task_definition}.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#capacity_provider_strategy EcsTaskSet#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetCapacityProviderStrategy]]], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#external_id EcsTaskSet#external_id}.'''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#force_delete EcsTaskSet#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#id EcsTaskSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#launch_type EcsTaskSet#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer EcsTaskSet#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsTaskSetLoadBalancer"]]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EcsTaskSetNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#network_configuration EcsTaskSet#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EcsTaskSetNetworkConfiguration"], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#platform_version EcsTaskSet#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale(self) -> typing.Optional["EcsTaskSetScale"]:
        '''scale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#scale EcsTaskSet#scale}
        '''
        result = self._values.get("scale")
        return typing.cast(typing.Optional["EcsTaskSetScale"], result)

    @builtins.property
    def service_registries(self) -> typing.Optional["EcsTaskSetServiceRegistries"]:
        '''service_registries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#service_registries EcsTaskSet#service_registries}
        '''
        result = self._values.get("service_registries")
        return typing.cast(typing.Optional["EcsTaskSetServiceRegistries"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags EcsTaskSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#tags_all EcsTaskSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def wait_until_stable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable EcsTaskSet#wait_until_stable}.'''
        result = self._values.get("wait_until_stable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def wait_until_stable_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#wait_until_stable_timeout EcsTaskSet#wait_until_stable_timeout}.'''
        result = self._values.get("wait_until_stable_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "load_balancer_name": "loadBalancerName",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsTaskSetLoadBalancer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: typing.Optional[jsii.Number] = None,
        load_balancer_name: typing.Optional[builtins.str] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param load_balancer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer_name EcsTaskSet#load_balancer_name}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#target_group_arn EcsTaskSet#target_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetLoadBalancer.__init__)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
        }
        if container_port is not None:
            self._values["container_port"] = container_port
        if load_balancer_name is not None:
            self._values["load_balancer_name"] = load_balancer_name
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_balancer_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#load_balancer_name EcsTaskSet#load_balancer_name}.'''
        result = self._values.get("load_balancer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#target_group_arn EcsTaskSet#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetLoadBalancerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetLoadBalancerList",
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
            type_hints = typing.get_type_hints(EcsTaskSetLoadBalancerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsTaskSetLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetLoadBalancerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsTaskSetLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsTaskSetLoadBalancer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsTaskSetLoadBalancerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskSetLoadBalancerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetLoadBalancerName")
    def reset_load_balancer_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerName", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerNameInput")
    def load_balancer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerOutputReference, "container_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerName"))

    @load_balancer_name.setter
    def load_balancer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerOutputReference, "load_balancer_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerName", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerOutputReference, "target_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsTaskSetLoadBalancer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsTaskSetLoadBalancer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsTaskSetLoadBalancer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetLoadBalancerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class EcsTaskSetNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetNetworkConfiguration.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#subnets EcsTaskSet#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#assign_public_ip EcsTaskSet#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#security_groups EcsTaskSet#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskSetNetworkConfigurationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EcsTaskSetNetworkConfigurationOutputReference, "assign_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetNetworkConfigurationOutputReference, "security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetNetworkConfigurationOutputReference, "subnets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetNetworkConfiguration]:
        return typing.cast(typing.Optional[EcsTaskSetNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskSetNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetScale",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class EcsTaskSetScale:
    def __init__(
        self,
        *,
        unit: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetScale.__init__)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if unit is not None:
            self._values["unit"] = unit
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#unit EcsTaskSet#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#value EcsTaskSet#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetScaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetScaleOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskSetScaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetScaleOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetScaleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetScale]:
        return typing.cast(typing.Optional[EcsTaskSetScale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EcsTaskSetScale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetScaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetServiceRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "registry_arn": "registryArn",
        "container_name": "containerName",
        "container_port": "containerPort",
        "port": "port",
    },
)
class EcsTaskSetServiceRegistries:
    def __init__(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EcsTaskSetServiceRegistries.__init__)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_arn": registry_arn,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#registry_arn EcsTaskSet#registry_arn}.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_name EcsTaskSet#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#container_port EcsTaskSet#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_task_set#port EcsTaskSet#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskSetServiceRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsTaskSetServiceRegistriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecs.EcsTaskSetServiceRegistriesOutputReference",
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
            type_hints = typing.get_type_hints(EcsTaskSetServiceRegistriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="registryArnInput")
    def registry_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetServiceRegistriesOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetServiceRegistriesOutputReference, "container_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetServiceRegistriesOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="registryArn")
    def registry_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryArn"))

    @registry_arn.setter
    def registry_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetServiceRegistriesOutputReference, "registry_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsTaskSetServiceRegistries]:
        return typing.cast(typing.Optional[EcsTaskSetServiceRegistries], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsTaskSetServiceRegistries],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EcsTaskSetServiceRegistriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsEcsCluster",
    "DataAwsEcsClusterConfig",
    "DataAwsEcsClusterSetting",
    "DataAwsEcsClusterSettingList",
    "DataAwsEcsClusterSettingOutputReference",
    "DataAwsEcsContainerDefinition",
    "DataAwsEcsContainerDefinitionConfig",
    "DataAwsEcsService",
    "DataAwsEcsServiceConfig",
    "DataAwsEcsTaskDefinition",
    "DataAwsEcsTaskDefinitionConfig",
    "EcsAccountSettingDefault",
    "EcsAccountSettingDefaultConfig",
    "EcsCapacityProvider",
    "EcsCapacityProviderAutoScalingGroupProvider",
    "EcsCapacityProviderAutoScalingGroupProviderManagedScaling",
    "EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference",
    "EcsCapacityProviderAutoScalingGroupProviderOutputReference",
    "EcsCapacityProviderConfig",
    "EcsCluster",
    "EcsClusterCapacityProviders",
    "EcsClusterCapacityProvidersConfig",
    "EcsClusterCapacityProvidersDefaultCapacityProviderStrategy",
    "EcsClusterCapacityProvidersDefaultCapacityProviderStrategyList",
    "EcsClusterCapacityProvidersDefaultCapacityProviderStrategyOutputReference",
    "EcsClusterConfig",
    "EcsClusterConfiguration",
    "EcsClusterConfigurationExecuteCommandConfiguration",
    "EcsClusterConfigurationExecuteCommandConfigurationLogConfiguration",
    "EcsClusterConfigurationExecuteCommandConfigurationLogConfigurationOutputReference",
    "EcsClusterConfigurationExecuteCommandConfigurationOutputReference",
    "EcsClusterConfigurationOutputReference",
    "EcsClusterDefaultCapacityProviderStrategy",
    "EcsClusterDefaultCapacityProviderStrategyList",
    "EcsClusterDefaultCapacityProviderStrategyOutputReference",
    "EcsClusterSetting",
    "EcsClusterSettingList",
    "EcsClusterSettingOutputReference",
    "EcsService",
    "EcsServiceCapacityProviderStrategy",
    "EcsServiceCapacityProviderStrategyList",
    "EcsServiceCapacityProviderStrategyOutputReference",
    "EcsServiceConfig",
    "EcsServiceDeploymentCircuitBreaker",
    "EcsServiceDeploymentCircuitBreakerOutputReference",
    "EcsServiceDeploymentController",
    "EcsServiceDeploymentControllerOutputReference",
    "EcsServiceLoadBalancer",
    "EcsServiceLoadBalancerList",
    "EcsServiceLoadBalancerOutputReference",
    "EcsServiceNetworkConfiguration",
    "EcsServiceNetworkConfigurationOutputReference",
    "EcsServiceOrderedPlacementStrategy",
    "EcsServiceOrderedPlacementStrategyList",
    "EcsServiceOrderedPlacementStrategyOutputReference",
    "EcsServicePlacementConstraints",
    "EcsServicePlacementConstraintsList",
    "EcsServicePlacementConstraintsOutputReference",
    "EcsServiceServiceRegistries",
    "EcsServiceServiceRegistriesOutputReference",
    "EcsServiceTimeouts",
    "EcsServiceTimeoutsOutputReference",
    "EcsTag",
    "EcsTagConfig",
    "EcsTaskDefinition",
    "EcsTaskDefinitionConfig",
    "EcsTaskDefinitionEphemeralStorage",
    "EcsTaskDefinitionEphemeralStorageOutputReference",
    "EcsTaskDefinitionInferenceAccelerator",
    "EcsTaskDefinitionInferenceAcceleratorList",
    "EcsTaskDefinitionInferenceAcceleratorOutputReference",
    "EcsTaskDefinitionPlacementConstraints",
    "EcsTaskDefinitionPlacementConstraintsList",
    "EcsTaskDefinitionPlacementConstraintsOutputReference",
    "EcsTaskDefinitionProxyConfiguration",
    "EcsTaskDefinitionProxyConfigurationOutputReference",
    "EcsTaskDefinitionRuntimePlatform",
    "EcsTaskDefinitionRuntimePlatformOutputReference",
    "EcsTaskDefinitionVolume",
    "EcsTaskDefinitionVolumeDockerVolumeConfiguration",
    "EcsTaskDefinitionVolumeDockerVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeEfsVolumeConfiguration",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigOutputReference",
    "EcsTaskDefinitionVolumeEfsVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigOutputReference",
    "EcsTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationOutputReference",
    "EcsTaskDefinitionVolumeList",
    "EcsTaskDefinitionVolumeOutputReference",
    "EcsTaskSet",
    "EcsTaskSetCapacityProviderStrategy",
    "EcsTaskSetCapacityProviderStrategyList",
    "EcsTaskSetCapacityProviderStrategyOutputReference",
    "EcsTaskSetConfig",
    "EcsTaskSetLoadBalancer",
    "EcsTaskSetLoadBalancerList",
    "EcsTaskSetLoadBalancerOutputReference",
    "EcsTaskSetNetworkConfiguration",
    "EcsTaskSetNetworkConfigurationOutputReference",
    "EcsTaskSetScale",
    "EcsTaskSetScaleOutputReference",
    "EcsTaskSetServiceRegistries",
    "EcsTaskSetServiceRegistriesOutputReference",
]

publication.publish()
