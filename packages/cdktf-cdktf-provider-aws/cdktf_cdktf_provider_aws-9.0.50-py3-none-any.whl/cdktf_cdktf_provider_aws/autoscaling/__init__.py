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


class AutoscalingAttachment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingAttachment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment aws_autoscaling_attachment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        alb_target_group_arn: typing.Optional[builtins.str] = None,
        elb: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lb_target_group_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment aws_autoscaling_attachment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#autoscaling_group_name AutoscalingAttachment#autoscaling_group_name}.
        :param alb_target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#alb_target_group_arn AutoscalingAttachment#alb_target_group_arn}.
        :param elb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#elb AutoscalingAttachment#elb}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#id AutoscalingAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lb_target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#lb_target_group_arn AutoscalingAttachment#lb_target_group_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingAttachmentConfig(
            autoscaling_group_name=autoscaling_group_name,
            alb_target_group_arn=alb_target_group_arn,
            elb=elb,
            id=id,
            lb_target_group_arn=lb_target_group_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAlbTargetGroupArn")
    def reset_alb_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlbTargetGroupArn", []))

    @jsii.member(jsii_name="resetElb")
    def reset_elb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElb", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLbTargetGroupArn")
    def reset_lb_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLbTargetGroupArn", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="albTargetGroupArnInput")
    def alb_target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "albTargetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="elbInput")
    def elb_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elbInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lbTargetGroupArnInput")
    def lb_target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lbTargetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="albTargetGroupArn")
    def alb_target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "albTargetGroupArn"))

    @alb_target_group_arn.setter
    def alb_target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingAttachment, "alb_target_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "albTargetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingAttachment, "autoscaling_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="elb")
    def elb(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elb"))

    @elb.setter
    def elb(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingAttachment, "elb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elb", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingAttachment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lbTargetGroupArn")
    def lb_target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lbTargetGroupArn"))

    @lb_target_group_arn.setter
    def lb_target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingAttachment, "lb_target_group_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lbTargetGroupArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingAttachmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "alb_target_group_arn": "albTargetGroupArn",
        "elb": "elb",
        "id": "id",
        "lb_target_group_arn": "lbTargetGroupArn",
    },
)
class AutoscalingAttachmentConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        alb_target_group_arn: typing.Optional[builtins.str] = None,
        elb: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lb_target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#autoscaling_group_name AutoscalingAttachment#autoscaling_group_name}.
        :param alb_target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#alb_target_group_arn AutoscalingAttachment#alb_target_group_arn}.
        :param elb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#elb AutoscalingAttachment#elb}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#id AutoscalingAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lb_target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#lb_target_group_arn AutoscalingAttachment#lb_target_group_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingAttachmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument alb_target_group_arn", value=alb_target_group_arn, expected_type=type_hints["alb_target_group_arn"])
            check_type(argname="argument elb", value=elb, expected_type=type_hints["elb"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lb_target_group_arn", value=lb_target_group_arn, expected_type=type_hints["lb_target_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
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
        if alb_target_group_arn is not None:
            self._values["alb_target_group_arn"] = alb_target_group_arn
        if elb is not None:
            self._values["elb"] = elb
        if id is not None:
            self._values["id"] = id
        if lb_target_group_arn is not None:
            self._values["lb_target_group_arn"] = lb_target_group_arn

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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#autoscaling_group_name AutoscalingAttachment#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alb_target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#alb_target_group_arn AutoscalingAttachment#alb_target_group_arn}.'''
        result = self._values.get("alb_target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elb(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#elb AutoscalingAttachment#elb}.'''
        result = self._values.get("elb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#id AutoscalingAttachment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lb_target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_attachment#lb_target_group_arn AutoscalingAttachment#lb_target_group_arn}.'''
        result = self._values.get("lb_target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingAttachmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group aws_autoscaling_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        max_size: jsii.Number,
        min_size: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        context: typing.Optional[builtins.str] = None,
        default_cooldown: typing.Optional[jsii.Number] = None,
        default_instance_warmup: typing.Optional[jsii.Number] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]]] = None,
        instance_refresh: typing.Optional[typing.Union["AutoscalingGroupInstanceRefresh", typing.Dict[str, typing.Any]]] = None,
        launch_configuration: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["AutoscalingGroupLaunchTemplate", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_instance_lifetime: typing.Optional[jsii.Number] = None,
        metrics_granularity: typing.Optional[builtins.str] = None,
        min_elb_capacity: typing.Optional[jsii.Number] = None,
        mixed_instances_policy: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicy", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_group: typing.Optional[builtins.str] = None,
        protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_linked_role_arn: typing.Optional[builtins.str] = None,
        suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutoscalingGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
        wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
        warm_pool: typing.Optional[typing.Union["AutoscalingGroupWarmPool", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group aws_autoscaling_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.
        :param capacity_rebalance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.
        :param default_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.
        :param default_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.
        :param enabled_metrics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.
        :param force_delete_warm_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_lifecycle_hook: initial_lifecycle_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        :param instance_refresh: instance_refresh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        :param launch_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param load_balancers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.
        :param max_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.
        :param metrics_granularity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.
        :param min_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.
        :param mixed_instances_policy: mixed_instances_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.
        :param protect_from_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.
        :param service_linked_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.
        :param suspended_processes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.
        :param target_group_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.
        :param termination_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        :param vpc_zone_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.
        :param wait_for_capacity_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.
        :param wait_for_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.
        :param warm_pool: warm_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingGroupConfig(
            max_size=max_size,
            min_size=min_size,
            availability_zones=availability_zones,
            capacity_rebalance=capacity_rebalance,
            context=context,
            default_cooldown=default_cooldown,
            default_instance_warmup=default_instance_warmup,
            desired_capacity=desired_capacity,
            enabled_metrics=enabled_metrics,
            force_delete=force_delete,
            force_delete_warm_pool=force_delete_warm_pool,
            health_check_grace_period=health_check_grace_period,
            health_check_type=health_check_type,
            id=id,
            initial_lifecycle_hook=initial_lifecycle_hook,
            instance_refresh=instance_refresh,
            launch_configuration=launch_configuration,
            launch_template=launch_template,
            load_balancers=load_balancers,
            max_instance_lifetime=max_instance_lifetime,
            metrics_granularity=metrics_granularity,
            min_elb_capacity=min_elb_capacity,
            mixed_instances_policy=mixed_instances_policy,
            name=name,
            name_prefix=name_prefix,
            placement_group=placement_group,
            protect_from_scale_in=protect_from_scale_in,
            service_linked_role_arn=service_linked_role_arn,
            suspended_processes=suspended_processes,
            tag=tag,
            tags=tags,
            target_group_arns=target_group_arns,
            termination_policies=termination_policies,
            timeouts=timeouts,
            vpc_zone_identifier=vpc_zone_identifier,
            wait_for_capacity_timeout=wait_for_capacity_timeout,
            wait_for_elb_capacity=wait_for_elb_capacity,
            warm_pool=warm_pool,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInitialLifecycleHook")
    def put_initial_lifecycle_hook(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroup.put_initial_lifecycle_hook)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitialLifecycleHook", [value]))

    @jsii.member(jsii_name="putInstanceRefresh")
    def put_instance_refresh(
        self,
        *,
        strategy: builtins.str,
        preferences: typing.Optional[typing.Union["AutoscalingGroupInstanceRefreshPreferences", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.
        :param preferences: preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.
        '''
        value = AutoscalingGroupInstanceRefresh(
            strategy=strategy, preferences=preferences, triggers=triggers
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceRefresh", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupLaunchTemplate(id=id, name=name, version=version)

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="putMixedInstancesPolicy")
    def put_mixed_instances_policy(
        self,
        *,
        launch_template: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplate", typing.Dict[str, typing.Any]],
        instances_distribution: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyInstancesDistribution", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param instances_distribution: instances_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        value = AutoscalingGroupMixedInstancesPolicy(
            launch_template=launch_template,
            instances_distribution=instances_distribution,
        )

        return typing.cast(None, jsii.invoke(self, "putMixedInstancesPolicy", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroup.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.
        '''
        value = AutoscalingGroupTimeouts(delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWarmPool")
    def put_warm_pool(
        self,
        *,
        instance_reuse_policy: typing.Optional[typing.Union["AutoscalingGroupWarmPoolInstanceReusePolicy", typing.Dict[str, typing.Any]]] = None,
        max_group_prepared_capacity: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        pool_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_reuse_policy: instance_reuse_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        :param max_group_prepared_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param pool_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.
        '''
        value = AutoscalingGroupWarmPool(
            instance_reuse_policy=instance_reuse_policy,
            max_group_prepared_capacity=max_group_prepared_capacity,
            min_size=min_size,
            pool_state=pool_state,
        )

        return typing.cast(None, jsii.invoke(self, "putWarmPool", [value]))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetCapacityRebalance")
    def reset_capacity_rebalance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityRebalance", []))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetDefaultCooldown")
    def reset_default_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultCooldown", []))

    @jsii.member(jsii_name="resetDefaultInstanceWarmup")
    def reset_default_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultInstanceWarmup", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetEnabledMetrics")
    def reset_enabled_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledMetrics", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetForceDeleteWarmPool")
    def reset_force_delete_warm_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDeleteWarmPool", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriod")
    def reset_health_check_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriod", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialLifecycleHook")
    def reset_initial_lifecycle_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialLifecycleHook", []))

    @jsii.member(jsii_name="resetInstanceRefresh")
    def reset_instance_refresh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRefresh", []))

    @jsii.member(jsii_name="resetLaunchConfiguration")
    def reset_launch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchConfiguration", []))

    @jsii.member(jsii_name="resetLaunchTemplate")
    def reset_launch_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplate", []))

    @jsii.member(jsii_name="resetLoadBalancers")
    def reset_load_balancers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancers", []))

    @jsii.member(jsii_name="resetMaxInstanceLifetime")
    def reset_max_instance_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxInstanceLifetime", []))

    @jsii.member(jsii_name="resetMetricsGranularity")
    def reset_metrics_granularity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsGranularity", []))

    @jsii.member(jsii_name="resetMinElbCapacity")
    def reset_min_elb_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinElbCapacity", []))

    @jsii.member(jsii_name="resetMixedInstancesPolicy")
    def reset_mixed_instances_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMixedInstancesPolicy", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPlacementGroup")
    def reset_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementGroup", []))

    @jsii.member(jsii_name="resetProtectFromScaleIn")
    def reset_protect_from_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectFromScaleIn", []))

    @jsii.member(jsii_name="resetServiceLinkedRoleArn")
    def reset_service_linked_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceLinkedRoleArn", []))

    @jsii.member(jsii_name="resetSuspendedProcesses")
    def reset_suspended_processes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspendedProcesses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTargetGroupArns")
    def reset_target_group_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArns", []))

    @jsii.member(jsii_name="resetTerminationPolicies")
    def reset_termination_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationPolicies", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcZoneIdentifier")
    def reset_vpc_zone_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcZoneIdentifier", []))

    @jsii.member(jsii_name="resetWaitForCapacityTimeout")
    def reset_wait_for_capacity_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForCapacityTimeout", []))

    @jsii.member(jsii_name="resetWaitForElbCapacity")
    def reset_wait_for_elb_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForElbCapacity", []))

    @jsii.member(jsii_name="resetWarmPool")
    def reset_warm_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmPool", []))

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
    @jsii.member(jsii_name="initialLifecycleHook")
    def initial_lifecycle_hook(self) -> "AutoscalingGroupInitialLifecycleHookList":
        return typing.cast("AutoscalingGroupInitialLifecycleHookList", jsii.get(self, "initialLifecycleHook"))

    @builtins.property
    @jsii.member(jsii_name="instanceRefresh")
    def instance_refresh(self) -> "AutoscalingGroupInstanceRefreshOutputReference":
        return typing.cast("AutoscalingGroupInstanceRefreshOutputReference", jsii.get(self, "instanceRefresh"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> "AutoscalingGroupLaunchTemplateOutputReference":
        return typing.cast("AutoscalingGroupLaunchTemplateOutputReference", jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="mixedInstancesPolicy")
    def mixed_instances_policy(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyOutputReference", jsii.get(self, "mixedInstancesPolicy"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "AutoscalingGroupTagList":
        return typing.cast("AutoscalingGroupTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AutoscalingGroupTimeoutsOutputReference":
        return typing.cast("AutoscalingGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="warmPool")
    def warm_pool(self) -> "AutoscalingGroupWarmPoolOutputReference":
        return typing.cast("AutoscalingGroupWarmPoolOutputReference", jsii.get(self, "warmPool"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityRebalanceInput")
    def capacity_rebalance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "capacityRebalanceInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCooldownInput")
    def default_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceWarmupInput")
    def default_instance_warmup_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInstanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledMetricsInput")
    def enabled_metrics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteWarmPoolInput")
    def force_delete_warm_pool_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteWarmPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodInput")
    def health_check_grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialLifecycleHookInput")
    def initial_lifecycle_hook_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]], jsii.get(self, "initialLifecycleHookInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceRefreshInput")
    def instance_refresh_input(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefresh"]:
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefresh"], jsii.get(self, "instanceRefreshInput"))

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationInput")
    def launch_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional["AutoscalingGroupLaunchTemplate"]:
        return typing.cast(typing.Optional["AutoscalingGroupLaunchTemplate"], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancersInput")
    def load_balancers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstanceLifetimeInput")
    def max_instance_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstanceLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsGranularityInput")
    def metrics_granularity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricsGranularityInput"))

    @builtins.property
    @jsii.member(jsii_name="minElbCapacityInput")
    def min_elb_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minElbCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="mixedInstancesPolicyInput")
    def mixed_instances_policy_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicy"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicy"], jsii.get(self, "mixedInstancesPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="placementGroupInput")
    def placement_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="protectFromScaleInInput")
    def protect_from_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "protectFromScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleArnInput")
    def service_linked_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceLinkedRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendedProcessesInput")
    def suspended_processes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "suspendedProcessesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnsInput")
    def target_group_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetGroupArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationPoliciesInput")
    def termination_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "terminationPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AutoscalingGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AutoscalingGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcZoneIdentifierInput")
    def vpc_zone_identifier_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcZoneIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForCapacityTimeoutInput")
    def wait_for_capacity_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForCapacityTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForElbCapacityInput")
    def wait_for_elb_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForElbCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="warmPoolInput")
    def warm_pool_input(self) -> typing.Optional["AutoscalingGroupWarmPool"]:
        return typing.cast(typing.Optional["AutoscalingGroupWarmPool"], jsii.get(self, "warmPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "availability_zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="capacityRebalance")
    def capacity_rebalance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "capacityRebalance"))

    @capacity_rebalance.setter
    def capacity_rebalance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "capacity_rebalance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityRebalance", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "context").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="defaultCooldown")
    def default_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultCooldown"))

    @default_cooldown.setter
    def default_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "default_cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceWarmup")
    def default_instance_warmup(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultInstanceWarmup"))

    @default_instance_warmup.setter
    def default_instance_warmup(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "default_instance_warmup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultInstanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="enabledMetrics")
    def enabled_metrics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledMetrics"))

    @enabled_metrics.setter
    def enabled_metrics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "enabled_metrics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledMetrics", value)

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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="forceDeleteWarmPool")
    def force_delete_warm_pool(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDeleteWarmPool"))

    @force_delete_warm_pool.setter
    def force_delete_warm_pool(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "force_delete_warm_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDeleteWarmPool", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriod"))

    @health_check_grace_period.setter
    def health_check_grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "health_check_grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "health_check_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="launchConfiguration")
    def launch_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchConfiguration"))

    @launch_configuration.setter
    def launch_configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "launch_configuration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancers"))

    @load_balancers.setter
    def load_balancers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "load_balancers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancers", value)

    @builtins.property
    @jsii.member(jsii_name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstanceLifetime"))

    @max_instance_lifetime.setter
    def max_instance_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "max_instance_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstanceLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="metricsGranularity")
    def metrics_granularity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricsGranularity"))

    @metrics_granularity.setter
    def metrics_granularity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "metrics_granularity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsGranularity", value)

    @builtins.property
    @jsii.member(jsii_name="minElbCapacity")
    def min_elb_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minElbCapacity"))

    @min_elb_capacity.setter
    def min_elb_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "min_elb_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minElbCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementGroup"))

    @placement_group.setter
    def placement_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "placement_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="protectFromScaleIn")
    def protect_from_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "protectFromScaleIn"))

    @protect_from_scale_in.setter
    def protect_from_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "protect_from_scale_in").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectFromScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceLinkedRoleArn"))

    @service_linked_role_arn.setter
    def service_linked_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "service_linked_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceLinkedRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="suspendedProcesses")
    def suspended_processes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "suspendedProcesses"))

    @suspended_processes.setter
    def suspended_processes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "suspended_processes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspendedProcesses", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArns")
    def target_group_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetGroupArns"))

    @target_group_arns.setter
    def target_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "target_group_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="terminationPolicies")
    def termination_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "terminationPolicies"))

    @termination_policies.setter
    def termination_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "termination_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="vpcZoneIdentifier")
    def vpc_zone_identifier(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcZoneIdentifier"))

    @vpc_zone_identifier.setter
    def vpc_zone_identifier(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "vpc_zone_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcZoneIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="waitForCapacityTimeout")
    def wait_for_capacity_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitForCapacityTimeout"))

    @wait_for_capacity_timeout.setter
    def wait_for_capacity_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "wait_for_capacity_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForCapacityTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="waitForElbCapacity")
    def wait_for_elb_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitForElbCapacity"))

    @wait_for_elb_capacity.setter
    def wait_for_elb_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroup, "wait_for_elb_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForElbCapacity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "max_size": "maxSize",
        "min_size": "minSize",
        "availability_zones": "availabilityZones",
        "capacity_rebalance": "capacityRebalance",
        "context": "context",
        "default_cooldown": "defaultCooldown",
        "default_instance_warmup": "defaultInstanceWarmup",
        "desired_capacity": "desiredCapacity",
        "enabled_metrics": "enabledMetrics",
        "force_delete": "forceDelete",
        "force_delete_warm_pool": "forceDeleteWarmPool",
        "health_check_grace_period": "healthCheckGracePeriod",
        "health_check_type": "healthCheckType",
        "id": "id",
        "initial_lifecycle_hook": "initialLifecycleHook",
        "instance_refresh": "instanceRefresh",
        "launch_configuration": "launchConfiguration",
        "launch_template": "launchTemplate",
        "load_balancers": "loadBalancers",
        "max_instance_lifetime": "maxInstanceLifetime",
        "metrics_granularity": "metricsGranularity",
        "min_elb_capacity": "minElbCapacity",
        "mixed_instances_policy": "mixedInstancesPolicy",
        "name": "name",
        "name_prefix": "namePrefix",
        "placement_group": "placementGroup",
        "protect_from_scale_in": "protectFromScaleIn",
        "service_linked_role_arn": "serviceLinkedRoleArn",
        "suspended_processes": "suspendedProcesses",
        "tag": "tag",
        "tags": "tags",
        "target_group_arns": "targetGroupArns",
        "termination_policies": "terminationPolicies",
        "timeouts": "timeouts",
        "vpc_zone_identifier": "vpcZoneIdentifier",
        "wait_for_capacity_timeout": "waitForCapacityTimeout",
        "wait_for_elb_capacity": "waitForElbCapacity",
        "warm_pool": "warmPool",
    },
)
class AutoscalingGroupConfig(cdktf.TerraformMetaArguments):
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
        max_size: jsii.Number,
        min_size: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        context: typing.Optional[builtins.str] = None,
        default_cooldown: typing.Optional[jsii.Number] = None,
        default_instance_warmup: typing.Optional[jsii.Number] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]]] = None,
        instance_refresh: typing.Optional[typing.Union["AutoscalingGroupInstanceRefresh", typing.Dict[str, typing.Any]]] = None,
        launch_configuration: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["AutoscalingGroupLaunchTemplate", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_instance_lifetime: typing.Optional[jsii.Number] = None,
        metrics_granularity: typing.Optional[builtins.str] = None,
        min_elb_capacity: typing.Optional[jsii.Number] = None,
        mixed_instances_policy: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicy", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_group: typing.Optional[builtins.str] = None,
        protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_linked_role_arn: typing.Optional[builtins.str] = None,
        suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutoscalingGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
        wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
        warm_pool: typing.Optional[typing.Union["AutoscalingGroupWarmPool", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.
        :param capacity_rebalance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.
        :param default_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.
        :param default_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.
        :param enabled_metrics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.
        :param force_delete_warm_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_lifecycle_hook: initial_lifecycle_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        :param instance_refresh: instance_refresh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        :param launch_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param load_balancers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.
        :param max_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.
        :param metrics_granularity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.
        :param min_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.
        :param mixed_instances_policy: mixed_instances_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.
        :param protect_from_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.
        :param service_linked_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.
        :param suspended_processes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.
        :param target_group_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.
        :param termination_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        :param vpc_zone_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.
        :param wait_for_capacity_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.
        :param wait_for_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.
        :param warm_pool: warm_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(instance_refresh, dict):
            instance_refresh = AutoscalingGroupInstanceRefresh(**instance_refresh)
        if isinstance(launch_template, dict):
            launch_template = AutoscalingGroupLaunchTemplate(**launch_template)
        if isinstance(mixed_instances_policy, dict):
            mixed_instances_policy = AutoscalingGroupMixedInstancesPolicy(**mixed_instances_policy)
        if isinstance(timeouts, dict):
            timeouts = AutoscalingGroupTimeouts(**timeouts)
        if isinstance(warm_pool, dict):
            warm_pool = AutoscalingGroupWarmPool(**warm_pool)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument capacity_rebalance", value=capacity_rebalance, expected_type=type_hints["capacity_rebalance"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument default_cooldown", value=default_cooldown, expected_type=type_hints["default_cooldown"])
            check_type(argname="argument default_instance_warmup", value=default_instance_warmup, expected_type=type_hints["default_instance_warmup"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument enabled_metrics", value=enabled_metrics, expected_type=type_hints["enabled_metrics"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument force_delete_warm_pool", value=force_delete_warm_pool, expected_type=type_hints["force_delete_warm_pool"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_lifecycle_hook", value=initial_lifecycle_hook, expected_type=type_hints["initial_lifecycle_hook"])
            check_type(argname="argument instance_refresh", value=instance_refresh, expected_type=type_hints["instance_refresh"])
            check_type(argname="argument launch_configuration", value=launch_configuration, expected_type=type_hints["launch_configuration"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
            check_type(argname="argument max_instance_lifetime", value=max_instance_lifetime, expected_type=type_hints["max_instance_lifetime"])
            check_type(argname="argument metrics_granularity", value=metrics_granularity, expected_type=type_hints["metrics_granularity"])
            check_type(argname="argument min_elb_capacity", value=min_elb_capacity, expected_type=type_hints["min_elb_capacity"])
            check_type(argname="argument mixed_instances_policy", value=mixed_instances_policy, expected_type=type_hints["mixed_instances_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
            check_type(argname="argument protect_from_scale_in", value=protect_from_scale_in, expected_type=type_hints["protect_from_scale_in"])
            check_type(argname="argument service_linked_role_arn", value=service_linked_role_arn, expected_type=type_hints["service_linked_role_arn"])
            check_type(argname="argument suspended_processes", value=suspended_processes, expected_type=type_hints["suspended_processes"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_group_arns", value=target_group_arns, expected_type=type_hints["target_group_arns"])
            check_type(argname="argument termination_policies", value=termination_policies, expected_type=type_hints["termination_policies"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_zone_identifier", value=vpc_zone_identifier, expected_type=type_hints["vpc_zone_identifier"])
            check_type(argname="argument wait_for_capacity_timeout", value=wait_for_capacity_timeout, expected_type=type_hints["wait_for_capacity_timeout"])
            check_type(argname="argument wait_for_elb_capacity", value=wait_for_elb_capacity, expected_type=type_hints["wait_for_elb_capacity"])
            check_type(argname="argument warm_pool", value=warm_pool, expected_type=type_hints["warm_pool"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_size": max_size,
            "min_size": min_size,
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
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if capacity_rebalance is not None:
            self._values["capacity_rebalance"] = capacity_rebalance
        if context is not None:
            self._values["context"] = context
        if default_cooldown is not None:
            self._values["default_cooldown"] = default_cooldown
        if default_instance_warmup is not None:
            self._values["default_instance_warmup"] = default_instance_warmup
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if enabled_metrics is not None:
            self._values["enabled_metrics"] = enabled_metrics
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if force_delete_warm_pool is not None:
            self._values["force_delete_warm_pool"] = force_delete_warm_pool
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if id is not None:
            self._values["id"] = id
        if initial_lifecycle_hook is not None:
            self._values["initial_lifecycle_hook"] = initial_lifecycle_hook
        if instance_refresh is not None:
            self._values["instance_refresh"] = instance_refresh
        if launch_configuration is not None:
            self._values["launch_configuration"] = launch_configuration
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers
        if max_instance_lifetime is not None:
            self._values["max_instance_lifetime"] = max_instance_lifetime
        if metrics_granularity is not None:
            self._values["metrics_granularity"] = metrics_granularity
        if min_elb_capacity is not None:
            self._values["min_elb_capacity"] = min_elb_capacity
        if mixed_instances_policy is not None:
            self._values["mixed_instances_policy"] = mixed_instances_policy
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if placement_group is not None:
            self._values["placement_group"] = placement_group
        if protect_from_scale_in is not None:
            self._values["protect_from_scale_in"] = protect_from_scale_in
        if service_linked_role_arn is not None:
            self._values["service_linked_role_arn"] = service_linked_role_arn
        if suspended_processes is not None:
            self._values["suspended_processes"] = suspended_processes
        if tag is not None:
            self._values["tag"] = tag
        if tags is not None:
            self._values["tags"] = tags
        if target_group_arns is not None:
            self._values["target_group_arns"] = target_group_arns
        if termination_policies is not None:
            self._values["termination_policies"] = termination_policies
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_zone_identifier is not None:
            self._values["vpc_zone_identifier"] = vpc_zone_identifier
        if wait_for_capacity_timeout is not None:
            self._values["wait_for_capacity_timeout"] = wait_for_capacity_timeout
        if wait_for_elb_capacity is not None:
            self._values["wait_for_elb_capacity"] = wait_for_elb_capacity
        if warm_pool is not None:
            self._values["warm_pool"] = warm_pool

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
    def max_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.'''
        result = self._values.get("max_size")
        assert result is not None, "Required property 'max_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.'''
        result = self._values.get("min_size")
        assert result is not None, "Required property 'min_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def capacity_rebalance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.'''
        result = self._values.get("capacity_rebalance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.'''
        result = self._values.get("default_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_instance_warmup(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.'''
        result = self._values.get("default_instance_warmup")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled_metrics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.'''
        result = self._values.get("enabled_metrics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_delete_warm_pool(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.'''
        result = self._values.get("force_delete_warm_pool")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.'''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.'''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_lifecycle_hook(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]]:
        '''initial_lifecycle_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        '''
        result = self._values.get("initial_lifecycle_hook")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]], result)

    @builtins.property
    def instance_refresh(self) -> typing.Optional["AutoscalingGroupInstanceRefresh"]:
        '''instance_refresh block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        '''
        result = self._values.get("instance_refresh")
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefresh"], result)

    @builtins.property
    def launch_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.'''
        result = self._values.get("launch_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(self) -> typing.Optional["AutoscalingGroupLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["AutoscalingGroupLaunchTemplate"], result)

    @builtins.property
    def load_balancers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.'''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_instance_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.'''
        result = self._values.get("max_instance_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metrics_granularity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.'''
        result = self._values.get("metrics_granularity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_elb_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.'''
        result = self._values.get("min_elb_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mixed_instances_policy(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicy"]:
        '''mixed_instances_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        '''
        result = self._values.get("mixed_instances_policy")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicy"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.'''
        result = self._values.get("placement_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protect_from_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.'''
        result = self._values.get("protect_from_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_linked_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.'''
        result = self._values.get("service_linked_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspended_processes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.'''
        result = self._values.get("suspended_processes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.'''
        result = self._values.get("target_group_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def termination_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.'''
        result = self._values.get("termination_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AutoscalingGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AutoscalingGroupTimeouts"], result)

    @builtins.property
    def vpc_zone_identifier(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.'''
        result = self._values.get("vpc_zone_identifier")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wait_for_capacity_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.'''
        result = self._values.get("wait_for_capacity_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_elb_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.'''
        result = self._values.get("wait_for_elb_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_pool(self) -> typing.Optional["AutoscalingGroupWarmPool"]:
        '''warm_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
        '''
        result = self._values.get("warm_pool")
        return typing.cast(typing.Optional["AutoscalingGroupWarmPool"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInitialLifecycleHook",
    jsii_struct_bases=[],
    name_mapping={
        "lifecycle_transition": "lifecycleTransition",
        "name": "name",
        "default_result": "defaultResult",
        "heartbeat_timeout": "heartbeatTimeout",
        "notification_metadata": "notificationMetadata",
        "notification_target_arn": "notificationTargetArn",
        "role_arn": "roleArn",
    },
)
class AutoscalingGroupInitialLifecycleHook:
    def __init__(
        self,
        *,
        lifecycle_transition: builtins.str,
        name: builtins.str,
        default_result: typing.Optional[builtins.str] = None,
        heartbeat_timeout: typing.Optional[jsii.Number] = None,
        notification_metadata: typing.Optional[builtins.str] = None,
        notification_target_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lifecycle_transition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#lifecycle_transition AutoscalingGroup#lifecycle_transition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param default_result: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_result AutoscalingGroup#default_result}.
        :param heartbeat_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#heartbeat_timeout AutoscalingGroup#heartbeat_timeout}.
        :param notification_metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_metadata AutoscalingGroup#notification_metadata}.
        :param notification_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_target_arn AutoscalingGroup#notification_target_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#role_arn AutoscalingGroup#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupInitialLifecycleHook.__init__)
            check_type(argname="argument lifecycle_transition", value=lifecycle_transition, expected_type=type_hints["lifecycle_transition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_result", value=default_result, expected_type=type_hints["default_result"])
            check_type(argname="argument heartbeat_timeout", value=heartbeat_timeout, expected_type=type_hints["heartbeat_timeout"])
            check_type(argname="argument notification_metadata", value=notification_metadata, expected_type=type_hints["notification_metadata"])
            check_type(argname="argument notification_target_arn", value=notification_target_arn, expected_type=type_hints["notification_target_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "lifecycle_transition": lifecycle_transition,
            "name": name,
        }
        if default_result is not None:
            self._values["default_result"] = default_result
        if heartbeat_timeout is not None:
            self._values["heartbeat_timeout"] = heartbeat_timeout
        if notification_metadata is not None:
            self._values["notification_metadata"] = notification_metadata
        if notification_target_arn is not None:
            self._values["notification_target_arn"] = notification_target_arn
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def lifecycle_transition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#lifecycle_transition AutoscalingGroup#lifecycle_transition}.'''
        result = self._values.get("lifecycle_transition")
        assert result is not None, "Required property 'lifecycle_transition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_result(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_result AutoscalingGroup#default_result}.'''
        result = self._values.get("default_result")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#heartbeat_timeout AutoscalingGroup#heartbeat_timeout}.'''
        result = self._values.get("heartbeat_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notification_metadata(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_metadata AutoscalingGroup#notification_metadata}.'''
        result = self._values.get("notification_metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_target_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_target_arn AutoscalingGroup#notification_target_arn}.'''
        result = self._values.get("notification_target_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#role_arn AutoscalingGroup#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInitialLifecycleHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInitialLifecycleHookList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInitialLifecycleHookList",
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
            type_hints = typing.get_type_hints(AutoscalingGroupInitialLifecycleHookList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingGroupInitialLifecycleHookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupInitialLifecycleHookList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupInitialLifecycleHookOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupInitialLifecycleHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInitialLifecycleHookOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupInitialLifecycleHookOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefaultResult")
    def reset_default_result(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResult", []))

    @jsii.member(jsii_name="resetHeartbeatTimeout")
    def reset_heartbeat_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeartbeatTimeout", []))

    @jsii.member(jsii_name="resetNotificationMetadata")
    def reset_notification_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationMetadata", []))

    @jsii.member(jsii_name="resetNotificationTargetArn")
    def reset_notification_target_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTargetArn", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResultInput")
    def default_result_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultResultInput"))

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeoutInput")
    def heartbeat_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heartbeatTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransitionInput")
    def lifecycle_transition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationMetadataInput")
    def notification_metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArnInput")
    def notification_target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTargetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResult")
    def default_result(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultResult"))

    @default_result.setter
    def default_result(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "default_result").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultResult", value)

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeout")
    def heartbeat_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "heartbeatTimeout"))

    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "heartbeat_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "heartbeatTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransition")
    def lifecycle_transition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleTransition"))

    @lifecycle_transition.setter
    def lifecycle_transition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "lifecycle_transition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleTransition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationMetadata")
    def notification_metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationMetadata"))

    @notification_metadata.setter
    def notification_metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "notification_metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArn")
    def notification_target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTargetArn"))

    @notification_target_arn.setter
    def notification_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "notification_target_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInitialLifecycleHookOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInstanceRefresh",
    jsii_struct_bases=[],
    name_mapping={
        "strategy": "strategy",
        "preferences": "preferences",
        "triggers": "triggers",
    },
)
class AutoscalingGroupInstanceRefresh:
    def __init__(
        self,
        *,
        strategy: builtins.str,
        preferences: typing.Optional[typing.Union["AutoscalingGroupInstanceRefreshPreferences", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.
        :param preferences: preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.
        '''
        if isinstance(preferences, dict):
            preferences = AutoscalingGroupInstanceRefreshPreferences(**preferences)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupInstanceRefresh.__init__)
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument preferences", value=preferences, expected_type=type_hints["preferences"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[str, typing.Any] = {
            "strategy": strategy,
        }
        if preferences is not None:
            self._values["preferences"] = preferences
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.'''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preferences(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefreshPreferences"]:
        '''preferences block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        '''
        result = self._values.get("preferences")
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefreshPreferences"], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.'''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInstanceRefresh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInstanceRefreshOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInstanceRefreshOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupInstanceRefreshOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPreferences")
    def put_preferences(
        self,
        *,
        checkpoint_delay: typing.Optional[builtins.str] = None,
        checkpoint_percentages: typing.Optional[typing.Sequence[jsii.Number]] = None,
        instance_warmup: typing.Optional[builtins.str] = None,
        min_healthy_percentage: typing.Optional[jsii.Number] = None,
        skip_matching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param checkpoint_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.
        :param checkpoint_percentages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.
        :param instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.
        :param min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.
        :param skip_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.
        '''
        value = AutoscalingGroupInstanceRefreshPreferences(
            checkpoint_delay=checkpoint_delay,
            checkpoint_percentages=checkpoint_percentages,
            instance_warmup=instance_warmup,
            min_healthy_percentage=min_healthy_percentage,
            skip_matching=skip_matching,
        )

        return typing.cast(None, jsii.invoke(self, "putPreferences", [value]))

    @jsii.member(jsii_name="resetPreferences")
    def reset_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferences", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @builtins.property
    @jsii.member(jsii_name="preferences")
    def preferences(
        self,
    ) -> "AutoscalingGroupInstanceRefreshPreferencesOutputReference":
        return typing.cast("AutoscalingGroupInstanceRefreshPreferencesOutputReference", jsii.get(self, "preferences"))

    @builtins.property
    @jsii.member(jsii_name="preferencesInput")
    def preferences_input(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefreshPreferences"]:
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefreshPreferences"], jsii.get(self, "preferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshOutputReference, "strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshOutputReference, "triggers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupInstanceRefresh]:
        return typing.cast(typing.Optional[AutoscalingGroupInstanceRefresh], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupInstanceRefresh],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInstanceRefreshPreferences",
    jsii_struct_bases=[],
    name_mapping={
        "checkpoint_delay": "checkpointDelay",
        "checkpoint_percentages": "checkpointPercentages",
        "instance_warmup": "instanceWarmup",
        "min_healthy_percentage": "minHealthyPercentage",
        "skip_matching": "skipMatching",
    },
)
class AutoscalingGroupInstanceRefreshPreferences:
    def __init__(
        self,
        *,
        checkpoint_delay: typing.Optional[builtins.str] = None,
        checkpoint_percentages: typing.Optional[typing.Sequence[jsii.Number]] = None,
        instance_warmup: typing.Optional[builtins.str] = None,
        min_healthy_percentage: typing.Optional[jsii.Number] = None,
        skip_matching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param checkpoint_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.
        :param checkpoint_percentages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.
        :param instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.
        :param min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.
        :param skip_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupInstanceRefreshPreferences.__init__)
            check_type(argname="argument checkpoint_delay", value=checkpoint_delay, expected_type=type_hints["checkpoint_delay"])
            check_type(argname="argument checkpoint_percentages", value=checkpoint_percentages, expected_type=type_hints["checkpoint_percentages"])
            check_type(argname="argument instance_warmup", value=instance_warmup, expected_type=type_hints["instance_warmup"])
            check_type(argname="argument min_healthy_percentage", value=min_healthy_percentage, expected_type=type_hints["min_healthy_percentage"])
            check_type(argname="argument skip_matching", value=skip_matching, expected_type=type_hints["skip_matching"])
        self._values: typing.Dict[str, typing.Any] = {}
        if checkpoint_delay is not None:
            self._values["checkpoint_delay"] = checkpoint_delay
        if checkpoint_percentages is not None:
            self._values["checkpoint_percentages"] = checkpoint_percentages
        if instance_warmup is not None:
            self._values["instance_warmup"] = instance_warmup
        if min_healthy_percentage is not None:
            self._values["min_healthy_percentage"] = min_healthy_percentage
        if skip_matching is not None:
            self._values["skip_matching"] = skip_matching

    @builtins.property
    def checkpoint_delay(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.'''
        result = self._values.get("checkpoint_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def checkpoint_percentages(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.'''
        result = self._values.get("checkpoint_percentages")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def instance_warmup(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.'''
        result = self._values.get("instance_warmup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_healthy_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.'''
        result = self._values.get("min_healthy_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_matching(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.'''
        result = self._values.get("skip_matching")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInstanceRefreshPreferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInstanceRefreshPreferencesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupInstanceRefreshPreferencesOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupInstanceRefreshPreferencesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckpointDelay")
    def reset_checkpoint_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointDelay", []))

    @jsii.member(jsii_name="resetCheckpointPercentages")
    def reset_checkpoint_percentages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointPercentages", []))

    @jsii.member(jsii_name="resetInstanceWarmup")
    def reset_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceWarmup", []))

    @jsii.member(jsii_name="resetMinHealthyPercentage")
    def reset_min_healthy_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinHealthyPercentage", []))

    @jsii.member(jsii_name="resetSkipMatching")
    def reset_skip_matching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipMatching", []))

    @builtins.property
    @jsii.member(jsii_name="checkpointDelayInput")
    def checkpoint_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkpointDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointPercentagesInput")
    def checkpoint_percentages_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "checkpointPercentagesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupInput")
    def instance_warmup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="minHealthyPercentageInput")
    def min_healthy_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minHealthyPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="skipMatchingInput")
    def skip_matching_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipMatchingInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointDelay")
    def checkpoint_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkpointDelay"))

    @checkpoint_delay.setter
    def checkpoint_delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "checkpoint_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointDelay", value)

    @builtins.property
    @jsii.member(jsii_name="checkpointPercentages")
    def checkpoint_percentages(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "checkpointPercentages"))

    @checkpoint_percentages.setter
    def checkpoint_percentages(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "checkpoint_percentages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointPercentages", value)

    @builtins.property
    @jsii.member(jsii_name="instanceWarmup")
    def instance_warmup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceWarmup"))

    @instance_warmup.setter
    def instance_warmup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "instance_warmup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="minHealthyPercentage")
    def min_healthy_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minHealthyPercentage"))

    @min_healthy_percentage.setter
    def min_healthy_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "min_healthy_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minHealthyPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="skipMatching")
    def skip_matching(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipMatching"))

    @skip_matching.setter
    def skip_matching(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "skip_matching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipMatching", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupInstanceRefreshPreferences]:
        return typing.cast(typing.Optional[AutoscalingGroupInstanceRefreshPreferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupInstanceRefreshPreferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupInstanceRefreshPreferencesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name", "version": "version"},
)
class AutoscalingGroupLaunchTemplate:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupLaunchTemplate.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupLaunchTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupLaunchTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupLaunchTemplateOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupLaunchTemplateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupLaunchTemplateOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupLaunchTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template": "launchTemplate",
        "instances_distribution": "instancesDistribution",
    },
)
class AutoscalingGroupMixedInstancesPolicy:
    def __init__(
        self,
        *,
        launch_template: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplate", typing.Dict[str, typing.Any]],
        instances_distribution: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyInstancesDistribution", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param instances_distribution: instances_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        if isinstance(launch_template, dict):
            launch_template = AutoscalingGroupMixedInstancesPolicyLaunchTemplate(**launch_template)
        if isinstance(instances_distribution, dict):
            instances_distribution = AutoscalingGroupMixedInstancesPolicyInstancesDistribution(**instances_distribution)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicy.__init__)
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument instances_distribution", value=instances_distribution, expected_type=type_hints["instances_distribution"])
        self._values: typing.Dict[str, typing.Any] = {
            "launch_template": launch_template,
        }
        if instances_distribution is not None:
            self._values["instances_distribution"] = instances_distribution

    @builtins.property
    def launch_template(self) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplate":
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        '''
        result = self._values.get("launch_template")
        assert result is not None, "Required property 'launch_template' is missing"
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplate", result)

    @builtins.property
    def instances_distribution(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyInstancesDistribution"]:
        '''instances_distribution block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        result = self._values.get("instances_distribution")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyInstancesDistribution"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyInstancesDistribution",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_allocation_strategy": "onDemandAllocationStrategy",
        "on_demand_base_capacity": "onDemandBaseCapacity",
        "on_demand_percentage_above_base_capacity": "onDemandPercentageAboveBaseCapacity",
        "spot_allocation_strategy": "spotAllocationStrategy",
        "spot_instance_pools": "spotInstancePools",
        "spot_max_price": "spotMaxPrice",
    },
)
class AutoscalingGroupMixedInstancesPolicyInstancesDistribution:
    def __init__(
        self,
        *,
        on_demand_allocation_strategy: typing.Optional[builtins.str] = None,
        on_demand_base_capacity: typing.Optional[jsii.Number] = None,
        on_demand_percentage_above_base_capacity: typing.Optional[jsii.Number] = None,
        spot_allocation_strategy: typing.Optional[builtins.str] = None,
        spot_instance_pools: typing.Optional[jsii.Number] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param on_demand_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.
        :param on_demand_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.
        :param on_demand_percentage_above_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.
        :param spot_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.
        :param spot_instance_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.
        :param spot_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyInstancesDistribution.__init__)
            check_type(argname="argument on_demand_allocation_strategy", value=on_demand_allocation_strategy, expected_type=type_hints["on_demand_allocation_strategy"])
            check_type(argname="argument on_demand_base_capacity", value=on_demand_base_capacity, expected_type=type_hints["on_demand_base_capacity"])
            check_type(argname="argument on_demand_percentage_above_base_capacity", value=on_demand_percentage_above_base_capacity, expected_type=type_hints["on_demand_percentage_above_base_capacity"])
            check_type(argname="argument spot_allocation_strategy", value=spot_allocation_strategy, expected_type=type_hints["spot_allocation_strategy"])
            check_type(argname="argument spot_instance_pools", value=spot_instance_pools, expected_type=type_hints["spot_instance_pools"])
            check_type(argname="argument spot_max_price", value=spot_max_price, expected_type=type_hints["spot_max_price"])
        self._values: typing.Dict[str, typing.Any] = {}
        if on_demand_allocation_strategy is not None:
            self._values["on_demand_allocation_strategy"] = on_demand_allocation_strategy
        if on_demand_base_capacity is not None:
            self._values["on_demand_base_capacity"] = on_demand_base_capacity
        if on_demand_percentage_above_base_capacity is not None:
            self._values["on_demand_percentage_above_base_capacity"] = on_demand_percentage_above_base_capacity
        if spot_allocation_strategy is not None:
            self._values["spot_allocation_strategy"] = spot_allocation_strategy
        if spot_instance_pools is not None:
            self._values["spot_instance_pools"] = spot_instance_pools
        if spot_max_price is not None:
            self._values["spot_max_price"] = spot_max_price

    @builtins.property
    def on_demand_allocation_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.'''
        result = self._values.get("on_demand_allocation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_demand_base_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.'''
        result = self._values.get("on_demand_base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def on_demand_percentage_above_base_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.'''
        result = self._values.get("on_demand_percentage_above_base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_allocation_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.'''
        result = self._values.get("spot_allocation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_instance_pools(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.'''
        result = self._values.get("spot_instance_pools")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_max_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.'''
        result = self._values.get("spot_max_price")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyInstancesDistribution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOnDemandAllocationStrategy")
    def reset_on_demand_allocation_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandAllocationStrategy", []))

    @jsii.member(jsii_name="resetOnDemandBaseCapacity")
    def reset_on_demand_base_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandBaseCapacity", []))

    @jsii.member(jsii_name="resetOnDemandPercentageAboveBaseCapacity")
    def reset_on_demand_percentage_above_base_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandPercentageAboveBaseCapacity", []))

    @jsii.member(jsii_name="resetSpotAllocationStrategy")
    def reset_spot_allocation_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotAllocationStrategy", []))

    @jsii.member(jsii_name="resetSpotInstancePools")
    def reset_spot_instance_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotInstancePools", []))

    @jsii.member(jsii_name="resetSpotMaxPrice")
    def reset_spot_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="onDemandAllocationStrategyInput")
    def on_demand_allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onDemandAllocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandBaseCapacityInput")
    def on_demand_base_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandBaseCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandPercentageAboveBaseCapacityInput")
    def on_demand_percentage_above_base_capacity_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandPercentageAboveBaseCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="spotAllocationStrategyInput")
    def spot_allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotAllocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInstancePoolsInput")
    def spot_instance_pools_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotInstancePoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotMaxPriceInput")
    def spot_max_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotMaxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onDemandAllocationStrategy"))

    @on_demand_allocation_strategy.setter
    def on_demand_allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "on_demand_allocation_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandAllocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandBaseCapacity"))

    @on_demand_base_capacity.setter
    def on_demand_base_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "on_demand_base_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandBaseCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandPercentageAboveBaseCapacity"))

    @on_demand_percentage_above_base_capacity.setter
    def on_demand_percentage_above_base_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "on_demand_percentage_above_base_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandPercentageAboveBaseCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="spotAllocationStrategy")
    def spot_allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotAllocationStrategy"))

    @spot_allocation_strategy.setter
    def spot_allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "spot_allocation_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotAllocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="spotInstancePools")
    def spot_instance_pools(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotInstancePools"))

    @spot_instance_pools.setter
    def spot_instance_pools(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "spot_instance_pools").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstancePools", value)

    @builtins.property
    @jsii.member(jsii_name="spotMaxPrice")
    def spot_max_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotMaxPrice"))

    @spot_max_price.setter
    def spot_max_price(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "spot_max_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_specification": "launchTemplateSpecification",
        "override": "override",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplate:
    def __init__(
        self,
        *,
        launch_template_specification: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification", typing.Dict[str, typing.Any]],
        override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param override: override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        if isinstance(launch_template_specification, dict):
            launch_template_specification = AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(**launch_template_specification)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplate.__init__)
            check_type(argname="argument launch_template_specification", value=launch_template_specification, expected_type=type_hints["launch_template_specification"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "launch_template_specification": launch_template_specification,
        }
        if override is not None:
            self._values["override"] = override

    @builtins.property
    def launch_template_specification(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification":
        '''launch_template_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        '''
        result = self._values.get("launch_template_specification")
        assert result is not None, "Required property 'launch_template_specification' is missing"
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification", result)

    @builtins.property
    def override(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]]:
        '''override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        result = self._values.get("override")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "version": "version",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification.__init__)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, "launch_template_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, "launch_template_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLaunchTemplateSpecification")
    def put_launch_template_specification(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateSpecification", [value]))

    @jsii.member(jsii_name="putOverride")
    def put_override(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference.put_override)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverride", [value]))

    @jsii.member(jsii_name="resetOverride")
    def reset_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverride", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, jsii.get(self, "launchTemplateSpecification"))

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList", jsii.get(self, "override"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecificationInput")
    def launch_template_specification_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification], jsii.get(self, "launchTemplateSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride",
    jsii_struct_bases=[],
    name_mapping={
        "instance_requirements": "instanceRequirements",
        "instance_type": "instanceType",
        "launch_template_specification": "launchTemplateSpecification",
        "weighted_capacity": "weightedCapacity",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride:
    def __init__(
        self,
        *,
        instance_requirements: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements", typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        launch_template_specification: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification", typing.Dict[str, typing.Any]]] = None,
        weighted_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_requirements: instance_requirements block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_requirements AutoscalingGroup#instance_requirements}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_type AutoscalingGroup#instance_type}.
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#weighted_capacity AutoscalingGroup#weighted_capacity}.
        '''
        if isinstance(instance_requirements, dict):
            instance_requirements = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(**instance_requirements)
        if isinstance(launch_template_specification, dict):
            launch_template_specification = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(**launch_template_specification)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride.__init__)
            check_type(argname="argument instance_requirements", value=instance_requirements, expected_type=type_hints["instance_requirements"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument launch_template_specification", value=launch_template_specification, expected_type=type_hints["launch_template_specification"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_requirements is not None:
            self._values["instance_requirements"] = instance_requirements
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if launch_template_specification is not None:
            self._values["launch_template_specification"] = launch_template_specification
        if weighted_capacity is not None:
            self._values["weighted_capacity"] = weighted_capacity

    @builtins.property
    def instance_requirements(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements"]:
        '''instance_requirements block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_requirements AutoscalingGroup#instance_requirements}
        '''
        result = self._values.get("instance_requirements")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_type AutoscalingGroup#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_specification(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification"]:
        '''launch_template_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        '''
        result = self._values.get("launch_template_specification")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification"], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#weighted_capacity AutoscalingGroup#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_manufacturers": "acceleratorManufacturers",
        "accelerator_names": "acceleratorNames",
        "accelerator_total_memory_mib": "acceleratorTotalMemoryMib",
        "accelerator_types": "acceleratorTypes",
        "bare_metal": "bareMetal",
        "baseline_ebs_bandwidth_mbps": "baselineEbsBandwidthMbps",
        "burstable_performance": "burstablePerformance",
        "cpu_manufacturers": "cpuManufacturers",
        "excluded_instance_types": "excludedInstanceTypes",
        "instance_generations": "instanceGenerations",
        "local_storage": "localStorage",
        "local_storage_types": "localStorageTypes",
        "memory_gib_per_vcpu": "memoryGibPerVcpu",
        "memory_mib": "memoryMib",
        "network_interface_count": "networkInterfaceCount",
        "on_demand_max_price_percentage_over_lowest_price": "onDemandMaxPricePercentageOverLowestPrice",
        "require_hibernate_support": "requireHibernateSupport",
        "spot_max_price_percentage_over_lowest_price": "spotMaxPricePercentageOverLowestPrice",
        "total_local_storage_gb": "totalLocalStorageGb",
        "vcpu_count": "vcpuCount",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements:
    def __init__(
        self,
        *,
        accelerator_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount", typing.Dict[str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib", typing.Dict[str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps", typing.Dict[str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu", typing.Dict[str, typing.Any]]] = None,
        memory_mib: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib", typing.Dict[str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount", typing.Dict[str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb", typing.Dict[str, typing.Any]]] = None,
        vcpu_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        if isinstance(accelerator_count, dict):
            accelerator_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(**accelerator_count)
        if isinstance(accelerator_total_memory_mib, dict):
            accelerator_total_memory_mib = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(**accelerator_total_memory_mib)
        if isinstance(baseline_ebs_bandwidth_mbps, dict):
            baseline_ebs_bandwidth_mbps = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(**baseline_ebs_bandwidth_mbps)
        if isinstance(memory_gib_per_vcpu, dict):
            memory_gib_per_vcpu = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(**memory_gib_per_vcpu)
        if isinstance(memory_mib, dict):
            memory_mib = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(**memory_mib)
        if isinstance(network_interface_count, dict):
            network_interface_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(**network_interface_count)
        if isinstance(total_local_storage_gb, dict):
            total_local_storage_gb = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(**total_local_storage_gb)
        if isinstance(vcpu_count, dict):
            vcpu_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(**vcpu_count)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements.__init__)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_manufacturers", value=accelerator_manufacturers, expected_type=type_hints["accelerator_manufacturers"])
            check_type(argname="argument accelerator_names", value=accelerator_names, expected_type=type_hints["accelerator_names"])
            check_type(argname="argument accelerator_total_memory_mib", value=accelerator_total_memory_mib, expected_type=type_hints["accelerator_total_memory_mib"])
            check_type(argname="argument accelerator_types", value=accelerator_types, expected_type=type_hints["accelerator_types"])
            check_type(argname="argument bare_metal", value=bare_metal, expected_type=type_hints["bare_metal"])
            check_type(argname="argument baseline_ebs_bandwidth_mbps", value=baseline_ebs_bandwidth_mbps, expected_type=type_hints["baseline_ebs_bandwidth_mbps"])
            check_type(argname="argument burstable_performance", value=burstable_performance, expected_type=type_hints["burstable_performance"])
            check_type(argname="argument cpu_manufacturers", value=cpu_manufacturers, expected_type=type_hints["cpu_manufacturers"])
            check_type(argname="argument excluded_instance_types", value=excluded_instance_types, expected_type=type_hints["excluded_instance_types"])
            check_type(argname="argument instance_generations", value=instance_generations, expected_type=type_hints["instance_generations"])
            check_type(argname="argument local_storage", value=local_storage, expected_type=type_hints["local_storage"])
            check_type(argname="argument local_storage_types", value=local_storage_types, expected_type=type_hints["local_storage_types"])
            check_type(argname="argument memory_gib_per_vcpu", value=memory_gib_per_vcpu, expected_type=type_hints["memory_gib_per_vcpu"])
            check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
            check_type(argname="argument network_interface_count", value=network_interface_count, expected_type=type_hints["network_interface_count"])
            check_type(argname="argument on_demand_max_price_percentage_over_lowest_price", value=on_demand_max_price_percentage_over_lowest_price, expected_type=type_hints["on_demand_max_price_percentage_over_lowest_price"])
            check_type(argname="argument require_hibernate_support", value=require_hibernate_support, expected_type=type_hints["require_hibernate_support"])
            check_type(argname="argument spot_max_price_percentage_over_lowest_price", value=spot_max_price_percentage_over_lowest_price, expected_type=type_hints["spot_max_price_percentage_over_lowest_price"])
            check_type(argname="argument total_local_storage_gb", value=total_local_storage_gb, expected_type=type_hints["total_local_storage_gb"])
            check_type(argname="argument vcpu_count", value=vcpu_count, expected_type=type_hints["vcpu_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_manufacturers is not None:
            self._values["accelerator_manufacturers"] = accelerator_manufacturers
        if accelerator_names is not None:
            self._values["accelerator_names"] = accelerator_names
        if accelerator_total_memory_mib is not None:
            self._values["accelerator_total_memory_mib"] = accelerator_total_memory_mib
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if bare_metal is not None:
            self._values["bare_metal"] = bare_metal
        if baseline_ebs_bandwidth_mbps is not None:
            self._values["baseline_ebs_bandwidth_mbps"] = baseline_ebs_bandwidth_mbps
        if burstable_performance is not None:
            self._values["burstable_performance"] = burstable_performance
        if cpu_manufacturers is not None:
            self._values["cpu_manufacturers"] = cpu_manufacturers
        if excluded_instance_types is not None:
            self._values["excluded_instance_types"] = excluded_instance_types
        if instance_generations is not None:
            self._values["instance_generations"] = instance_generations
        if local_storage is not None:
            self._values["local_storage"] = local_storage
        if local_storage_types is not None:
            self._values["local_storage_types"] = local_storage_types
        if memory_gib_per_vcpu is not None:
            self._values["memory_gib_per_vcpu"] = memory_gib_per_vcpu
        if memory_mib is not None:
            self._values["memory_mib"] = memory_mib
        if network_interface_count is not None:
            self._values["network_interface_count"] = network_interface_count
        if on_demand_max_price_percentage_over_lowest_price is not None:
            self._values["on_demand_max_price_percentage_over_lowest_price"] = on_demand_max_price_percentage_over_lowest_price
        if require_hibernate_support is not None:
            self._values["require_hibernate_support"] = require_hibernate_support
        if spot_max_price_percentage_over_lowest_price is not None:
            self._values["spot_max_price_percentage_over_lowest_price"] = spot_max_price_percentage_over_lowest_price
        if total_local_storage_gb is not None:
            self._values["total_local_storage_gb"] = total_local_storage_gb
        if vcpu_count is not None:
            self._values["vcpu_count"] = vcpu_count

    @builtins.property
    def accelerator_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount"]:
        '''accelerator_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount"], result)

    @builtins.property
    def accelerator_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.'''
        result = self._values.get("accelerator_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.'''
        result = self._values.get("accelerator_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_total_memory_mib(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib"]:
        '''accelerator_total_memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        '''
        result = self._values.get("accelerator_total_memory_mib")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib"], result)

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.'''
        result = self._values.get("accelerator_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bare_metal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.'''
        result = self._values.get("bare_metal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps"]:
        '''baseline_ebs_bandwidth_mbps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        '''
        result = self._values.get("baseline_ebs_bandwidth_mbps")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps"], result)

    @builtins.property
    def burstable_performance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.'''
        result = self._values.get("burstable_performance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.'''
        result = self._values.get("cpu_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.'''
        result = self._values.get("excluded_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_generations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.'''
        result = self._values.get("instance_generations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def local_storage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.'''
        result = self._values.get("local_storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_storage_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.'''
        result = self._values.get("local_storage_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_gib_per_vcpu(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu"]:
        '''memory_gib_per_vcpu block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        '''
        result = self._values.get("memory_gib_per_vcpu")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu"], result)

    @builtins.property
    def memory_mib(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib"]:
        '''memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        '''
        result = self._values.get("memory_mib")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib"], result)

    @builtins.property
    def network_interface_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount"]:
        '''network_interface_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        '''
        result = self._values.get("network_interface_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount"], result)

    @builtins.property
    def on_demand_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("on_demand_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_hibernate_support(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.'''
        result = self._values.get("require_hibernate_support")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def spot_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("spot_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def total_local_storage_gb(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"]:
        '''total_local_storage_gb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        '''
        result = self._values.get("total_local_storage_gb")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"], result)

    @builtins.property
    def vcpu_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"]:
        '''vcpu_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        result = self._values.get("vcpu_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcceleratorCount")
    def put_accelerator_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorCount", [value]))

    @jsii.member(jsii_name="putAcceleratorTotalMemoryMib")
    def put_accelerator_total_memory_mib(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorTotalMemoryMib", [value]))

    @jsii.member(jsii_name="putBaselineEbsBandwidthMbps")
    def put_baseline_ebs_bandwidth_mbps(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putBaselineEbsBandwidthMbps", [value]))

    @jsii.member(jsii_name="putMemoryGibPerVcpu")
    def put_memory_gib_per_vcpu(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putMemoryGibPerVcpu", [value]))

    @jsii.member(jsii_name="putMemoryMib")
    def put_memory_mib(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putMemoryMib", [value]))

    @jsii.member(jsii_name="putNetworkInterfaceCount")
    def put_network_interface_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkInterfaceCount", [value]))

    @jsii.member(jsii_name="putTotalLocalStorageGb")
    def put_total_local_storage_gb(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putTotalLocalStorageGb", [value]))

    @jsii.member(jsii_name="putVcpuCount")
    def put_vcpu_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putVcpuCount", [value]))

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorManufacturers")
    def reset_accelerator_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorManufacturers", []))

    @jsii.member(jsii_name="resetAcceleratorNames")
    def reset_accelerator_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorNames", []))

    @jsii.member(jsii_name="resetAcceleratorTotalMemoryMib")
    def reset_accelerator_total_memory_mib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTotalMemoryMib", []))

    @jsii.member(jsii_name="resetAcceleratorTypes")
    def reset_accelerator_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTypes", []))

    @jsii.member(jsii_name="resetBareMetal")
    def reset_bare_metal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBareMetal", []))

    @jsii.member(jsii_name="resetBaselineEbsBandwidthMbps")
    def reset_baseline_ebs_bandwidth_mbps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineEbsBandwidthMbps", []))

    @jsii.member(jsii_name="resetBurstablePerformance")
    def reset_burstable_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBurstablePerformance", []))

    @jsii.member(jsii_name="resetCpuManufacturers")
    def reset_cpu_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuManufacturers", []))

    @jsii.member(jsii_name="resetExcludedInstanceTypes")
    def reset_excluded_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedInstanceTypes", []))

    @jsii.member(jsii_name="resetInstanceGenerations")
    def reset_instance_generations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceGenerations", []))

    @jsii.member(jsii_name="resetLocalStorage")
    def reset_local_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorage", []))

    @jsii.member(jsii_name="resetLocalStorageTypes")
    def reset_local_storage_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorageTypes", []))

    @jsii.member(jsii_name="resetMemoryGibPerVcpu")
    def reset_memory_gib_per_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGibPerVcpu", []))

    @jsii.member(jsii_name="resetMemoryMib")
    def reset_memory_mib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryMib", []))

    @jsii.member(jsii_name="resetNetworkInterfaceCount")
    def reset_network_interface_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterfaceCount", []))

    @jsii.member(jsii_name="resetOnDemandMaxPricePercentageOverLowestPrice")
    def reset_on_demand_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetRequireHibernateSupport")
    def reset_require_hibernate_support(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireHibernateSupport", []))

    @jsii.member(jsii_name="resetSpotMaxPricePercentageOverLowestPrice")
    def reset_spot_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetTotalLocalStorageGb")
    def reset_total_local_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalLocalStorageGb", []))

    @jsii.member(jsii_name="resetVcpuCount")
    def reset_vcpu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcpuCount", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference, jsii.get(self, "acceleratorCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, jsii.get(self, "acceleratorTotalMemoryMib"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, jsii.get(self, "baselineEbsBandwidthMbps"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference, jsii.get(self, "memoryGibPerVcpu"))

    @builtins.property
    @jsii.member(jsii_name="memoryMib")
    def memory_mib(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference, jsii.get(self, "memoryMib"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference, jsii.get(self, "networkInterfaceCount"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGb")
    def total_local_storage_gb(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference", jsii.get(self, "totalLocalStorageGb"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCount")
    def vcpu_count(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference", jsii.get(self, "vcpuCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturersInput")
    def accelerator_manufacturers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorNamesInput")
    def accelerator_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMibInput")
    def accelerator_total_memory_mib_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "acceleratorTotalMemoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypesInput")
    def accelerator_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="bareMetalInput")
    def bare_metal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bareMetalInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbpsInput")
    def baseline_ebs_bandwidth_mbps_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "baselineEbsBandwidthMbpsInput"))

    @builtins.property
    @jsii.member(jsii_name="burstablePerformanceInput")
    def burstable_performance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "burstablePerformanceInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturersInput")
    def cpu_manufacturers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cpuManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypesInput")
    def excluded_instance_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceGenerationsInput")
    def instance_generations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceGenerationsInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageInput")
    def local_storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageTypesInput")
    def local_storage_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localStorageTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpuInput")
    def memory_gib_per_vcpu_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "memoryGibPerVcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryMibInput")
    def memory_mib_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib], jsii.get(self, "memoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCountInput")
    def network_interface_count_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "networkInterfaceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPriceInput")
    def on_demand_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupportInput")
    def require_hibernate_support_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireHibernateSupportInput"))

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPriceInput")
    def spot_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGbInput")
    def total_local_storage_gb_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"], jsii.get(self, "totalLocalStorageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCountInput")
    def vcpu_count_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"], jsii.get(self, "vcpuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorManufacturers"))

    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "accelerator_manufacturers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorNames")
    def accelerator_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorNames"))

    @accelerator_names.setter
    def accelerator_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "accelerator_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorNames", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorTypes"))

    @accelerator_types.setter
    def accelerator_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "accelerator_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property
    @jsii.member(jsii_name="bareMetal")
    def bare_metal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bareMetal"))

    @bare_metal.setter
    def bare_metal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "bare_metal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bareMetal", value)

    @builtins.property
    @jsii.member(jsii_name="burstablePerformance")
    def burstable_performance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "burstablePerformance"))

    @burstable_performance.setter
    def burstable_performance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "burstable_performance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "burstablePerformance", value)

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturers")
    def cpu_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cpuManufacturers"))

    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "cpu_manufacturers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypes")
    def excluded_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedInstanceTypes"))

    @excluded_instance_types.setter
    def excluded_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "excluded_instance_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="instanceGenerations")
    def instance_generations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceGenerations"))

    @instance_generations.setter
    def instance_generations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "instance_generations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceGenerations", value)

    @builtins.property
    @jsii.member(jsii_name="localStorage")
    def local_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localStorage"))

    @local_storage.setter
    def local_storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "local_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorage", value)

    @builtins.property
    @jsii.member(jsii_name="localStorageTypes")
    def local_storage_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localStorageTypes"))

    @local_storage_types.setter
    def local_storage_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "local_storage_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorageTypes", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandMaxPricePercentageOverLowestPrice"))

    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "on_demand_max_price_percentage_over_lowest_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupport")
    def require_hibernate_support(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireHibernateSupport"))

    @require_hibernate_support.setter
    def require_hibernate_support(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "require_hibernate_support").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireHibernateSupport", value)

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotMaxPricePercentageOverLowestPrice"))

    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "spot_max_price_percentage_over_lowest_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "version": "version",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification.__init__)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, "launch_template_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, "launch_template_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putInstanceRequirements")
    def put_instance_requirements(
        self,
        *,
        accelerator_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount, typing.Dict[str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib, typing.Dict[str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps, typing.Dict[str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu, typing.Dict[str, typing.Any]]] = None,
        memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib, typing.Dict[str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount, typing.Dict[str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb, typing.Dict[str, typing.Any]]] = None,
        vcpu_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(
            accelerator_count=accelerator_count,
            accelerator_manufacturers=accelerator_manufacturers,
            accelerator_names=accelerator_names,
            accelerator_total_memory_mib=accelerator_total_memory_mib,
            accelerator_types=accelerator_types,
            bare_metal=bare_metal,
            baseline_ebs_bandwidth_mbps=baseline_ebs_bandwidth_mbps,
            burstable_performance=burstable_performance,
            cpu_manufacturers=cpu_manufacturers,
            excluded_instance_types=excluded_instance_types,
            instance_generations=instance_generations,
            local_storage=local_storage,
            local_storage_types=local_storage_types,
            memory_gib_per_vcpu=memory_gib_per_vcpu,
            memory_mib=memory_mib,
            network_interface_count=network_interface_count,
            on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
            require_hibernate_support=require_hibernate_support,
            spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
            total_local_storage_gb=total_local_storage_gb,
            vcpu_count=vcpu_count,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceRequirements", [value]))

    @jsii.member(jsii_name="putLaunchTemplateSpecification")
    def put_launch_template_specification(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateSpecification", [value]))

    @jsii.member(jsii_name="resetInstanceRequirements")
    def reset_instance_requirements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRequirements", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLaunchTemplateSpecification")
    def reset_launch_template_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateSpecification", []))

    @jsii.member(jsii_name="resetWeightedCapacity")
    def reset_weighted_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, jsii.get(self, "instanceRequirements"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, jsii.get(self, "launchTemplateSpecification"))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirementsInput")
    def instance_requirements_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements], jsii.get(self, "instanceRequirementsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecificationInput")
    def launch_template_specification_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification], jsii.get(self, "launchTemplateSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference, "instance_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference, "weighted_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupMixedInstancesPolicyOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupMixedInstancesPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstancesDistribution")
    def put_instances_distribution(
        self,
        *,
        on_demand_allocation_strategy: typing.Optional[builtins.str] = None,
        on_demand_base_capacity: typing.Optional[jsii.Number] = None,
        on_demand_percentage_above_base_capacity: typing.Optional[jsii.Number] = None,
        spot_allocation_strategy: typing.Optional[builtins.str] = None,
        spot_instance_pools: typing.Optional[jsii.Number] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param on_demand_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.
        :param on_demand_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.
        :param on_demand_percentage_above_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.
        :param spot_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.
        :param spot_instance_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.
        :param spot_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyInstancesDistribution(
            on_demand_allocation_strategy=on_demand_allocation_strategy,
            on_demand_base_capacity=on_demand_base_capacity,
            on_demand_percentage_above_base_capacity=on_demand_percentage_above_base_capacity,
            spot_allocation_strategy=spot_allocation_strategy,
            spot_instance_pools=spot_instance_pools,
            spot_max_price=spot_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putInstancesDistribution", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        launch_template_specification: typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification, typing.Dict[str, typing.Any]],
        override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param override: override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplate(
            launch_template_specification=launch_template_specification,
            override=override,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="resetInstancesDistribution")
    def reset_instances_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancesDistribution", []))

    @builtins.property
    @jsii.member(jsii_name="instancesDistribution")
    def instances_distribution(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, jsii.get(self, "instancesDistribution"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference, jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="instancesDistributionInput")
    def instances_distribution_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution], jsii.get(self, "instancesDistributionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupMixedInstancesPolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupMixedInstancesPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTag",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "propagate_at_launch": "propagateAtLaunch",
        "value": "value",
    },
)
class AutoscalingGroupTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        propagate_at_launch: typing.Union[builtins.bool, cdktf.IResolvable],
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#key AutoscalingGroup#key}.
        :param propagate_at_launch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#propagate_at_launch AutoscalingGroup#propagate_at_launch}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#value AutoscalingGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTag.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument propagate_at_launch", value=propagate_at_launch, expected_type=type_hints["propagate_at_launch"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "propagate_at_launch": propagate_at_launch,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#key AutoscalingGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#propagate_at_launch AutoscalingGroup#propagate_at_launch}.'''
        result = self._values.get("propagate_at_launch")
        assert result is not None, "Required property 'propagate_at_launch' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#value AutoscalingGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTagA(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag aws_autoscaling_group_tag}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        tag: typing.Union["AutoscalingGroupTagTag", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag aws_autoscaling_group_tag} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#autoscaling_group_name AutoscalingGroupTagA#autoscaling_group_name}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#tag AutoscalingGroupTagA#tag}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#id AutoscalingGroupTagA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTagA.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingGroupTagAConfig(
            autoscaling_group_name=autoscaling_group_name,
            tag=tag,
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

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        *,
        key: builtins.str,
        propagate_at_launch: typing.Union[builtins.bool, cdktf.IResolvable],
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#key AutoscalingGroupTagA#key}.
        :param propagate_at_launch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#propagate_at_launch AutoscalingGroupTagA#propagate_at_launch}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#value AutoscalingGroupTagA#value}.
        '''
        value_ = AutoscalingGroupTagTag(
            key=key, propagate_at_launch=propagate_at_launch, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putTag", [value_]))

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
    @jsii.member(jsii_name="tag")
    def tag(self) -> "AutoscalingGroupTagTagOutputReference":
        return typing.cast("AutoscalingGroupTagTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional["AutoscalingGroupTagTag"]:
        return typing.cast(typing.Optional["AutoscalingGroupTagTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagA, "autoscaling_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagA, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagAConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "tag": "tag",
        "id": "id",
    },
)
class AutoscalingGroupTagAConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        tag: typing.Union["AutoscalingGroupTagTag", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#autoscaling_group_name AutoscalingGroupTagA#autoscaling_group_name}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#tag AutoscalingGroupTagA#tag}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#id AutoscalingGroupTagA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tag, dict):
            tag = AutoscalingGroupTagTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTagAConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
            "tag": tag,
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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#autoscaling_group_name AutoscalingGroupTagA#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag(self) -> "AutoscalingGroupTagTag":
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#tag AutoscalingGroupTagA#tag}
        '''
        result = self._values.get("tag")
        assert result is not None, "Required property 'tag' is missing"
        return typing.cast("AutoscalingGroupTagTag", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#id AutoscalingGroupTagA#id}.

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
        return "AutoscalingGroupTagAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagList",
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
            type_hints = typing.get_type_hints(AutoscalingGroupTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AutoscalingGroupTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupTagOutputReference.__init__)
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
    @jsii.member(jsii_name="propagateAtLaunchInput")
    def propagate_at_launch_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "propagateAtLaunchInput"))

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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="propagateAtLaunch")
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "propagateAtLaunch"))

    @propagate_at_launch.setter
    def propagate_at_launch(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagOutputReference, "propagate_at_launch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateAtLaunch", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagTag",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "propagate_at_launch": "propagateAtLaunch",
        "value": "value",
    },
)
class AutoscalingGroupTagTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        propagate_at_launch: typing.Union[builtins.bool, cdktf.IResolvable],
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#key AutoscalingGroupTagA#key}.
        :param propagate_at_launch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#propagate_at_launch AutoscalingGroupTagA#propagate_at_launch}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#value AutoscalingGroupTagA#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTagTag.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument propagate_at_launch", value=propagate_at_launch, expected_type=type_hints["propagate_at_launch"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "propagate_at_launch": propagate_at_launch,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#key AutoscalingGroupTagA#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#propagate_at_launch AutoscalingGroupTagA#propagate_at_launch}.'''
        result = self._values.get("propagate_at_launch")
        assert result is not None, "Required property 'propagate_at_launch' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group_tag#value AutoscalingGroupTagA#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupTagTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTagTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTagTagOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupTagTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateAtLaunchInput")
    def propagate_at_launch_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "propagateAtLaunchInput"))

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
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagTagOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="propagateAtLaunch")
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "propagateAtLaunch"))

    @propagate_at_launch.setter
    def propagate_at_launch(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagTagOutputReference, "propagate_at_launch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateAtLaunch", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupTagTag]:
        return typing.cast(typing.Optional[AutoscalingGroupTagTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AutoscalingGroupTagTag]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTagTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete", "update": "update"},
)
class AutoscalingGroupTimeouts:
    def __init__(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupTimeouts.__init__)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupWarmPool",
    jsii_struct_bases=[],
    name_mapping={
        "instance_reuse_policy": "instanceReusePolicy",
        "max_group_prepared_capacity": "maxGroupPreparedCapacity",
        "min_size": "minSize",
        "pool_state": "poolState",
    },
)
class AutoscalingGroupWarmPool:
    def __init__(
        self,
        *,
        instance_reuse_policy: typing.Optional[typing.Union["AutoscalingGroupWarmPoolInstanceReusePolicy", typing.Dict[str, typing.Any]]] = None,
        max_group_prepared_capacity: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        pool_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_reuse_policy: instance_reuse_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        :param max_group_prepared_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param pool_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.
        '''
        if isinstance(instance_reuse_policy, dict):
            instance_reuse_policy = AutoscalingGroupWarmPoolInstanceReusePolicy(**instance_reuse_policy)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupWarmPool.__init__)
            check_type(argname="argument instance_reuse_policy", value=instance_reuse_policy, expected_type=type_hints["instance_reuse_policy"])
            check_type(argname="argument max_group_prepared_capacity", value=max_group_prepared_capacity, expected_type=type_hints["max_group_prepared_capacity"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument pool_state", value=pool_state, expected_type=type_hints["pool_state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_reuse_policy is not None:
            self._values["instance_reuse_policy"] = instance_reuse_policy
        if max_group_prepared_capacity is not None:
            self._values["max_group_prepared_capacity"] = max_group_prepared_capacity
        if min_size is not None:
            self._values["min_size"] = min_size
        if pool_state is not None:
            self._values["pool_state"] = pool_state

    @builtins.property
    def instance_reuse_policy(
        self,
    ) -> typing.Optional["AutoscalingGroupWarmPoolInstanceReusePolicy"]:
        '''instance_reuse_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        '''
        result = self._values.get("instance_reuse_policy")
        return typing.cast(typing.Optional["AutoscalingGroupWarmPoolInstanceReusePolicy"], result)

    @builtins.property
    def max_group_prepared_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.'''
        result = self._values.get("max_group_prepared_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pool_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.'''
        result = self._values.get("pool_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupWarmPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupWarmPoolInstanceReusePolicy",
    jsii_struct_bases=[],
    name_mapping={"reuse_on_scale_in": "reuseOnScaleIn"},
)
class AutoscalingGroupWarmPoolInstanceReusePolicy:
    def __init__(
        self,
        *,
        reuse_on_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reuse_on_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingGroupWarmPoolInstanceReusePolicy.__init__)
            check_type(argname="argument reuse_on_scale_in", value=reuse_on_scale_in, expected_type=type_hints["reuse_on_scale_in"])
        self._values: typing.Dict[str, typing.Any] = {}
        if reuse_on_scale_in is not None:
            self._values["reuse_on_scale_in"] = reuse_on_scale_in

    @builtins.property
    def reuse_on_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.'''
        result = self._values.get("reuse_on_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupWarmPoolInstanceReusePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReuseOnScaleIn")
    def reset_reuse_on_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReuseOnScaleIn", []))

    @builtins.property
    @jsii.member(jsii_name="reuseOnScaleInInput")
    def reuse_on_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reuseOnScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="reuseOnScaleIn")
    def reuse_on_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reuseOnScaleIn"))

    @reuse_on_scale_in.setter
    def reuse_on_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference, "reuse_on_scale_in").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reuseOnScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupWarmPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingGroupWarmPoolOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingGroupWarmPoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstanceReusePolicy")
    def put_instance_reuse_policy(
        self,
        *,
        reuse_on_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reuse_on_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.
        '''
        value = AutoscalingGroupWarmPoolInstanceReusePolicy(
            reuse_on_scale_in=reuse_on_scale_in
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceReusePolicy", [value]))

    @jsii.member(jsii_name="resetInstanceReusePolicy")
    def reset_instance_reuse_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceReusePolicy", []))

    @jsii.member(jsii_name="resetMaxGroupPreparedCapacity")
    def reset_max_group_prepared_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxGroupPreparedCapacity", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetPoolState")
    def reset_pool_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolState", []))

    @builtins.property
    @jsii.member(jsii_name="instanceReusePolicy")
    def instance_reuse_policy(
        self,
    ) -> AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference:
        return typing.cast(AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference, jsii.get(self, "instanceReusePolicy"))

    @builtins.property
    @jsii.member(jsii_name="instanceReusePolicyInput")
    def instance_reuse_policy_input(
        self,
    ) -> typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy], jsii.get(self, "instanceReusePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxGroupPreparedCapacityInput")
    def max_group_prepared_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxGroupPreparedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="poolStateInput")
    def pool_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolStateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxGroupPreparedCapacity"))

    @max_group_prepared_capacity.setter
    def max_group_prepared_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolOutputReference, "max_group_prepared_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxGroupPreparedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolOutputReference, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="poolState")
    def pool_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "poolState"))

    @pool_state.setter
    def pool_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolOutputReference, "pool_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupWarmPool]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AutoscalingGroupWarmPool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingGroupWarmPoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingLifecycleHook(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingLifecycleHook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook aws_autoscaling_lifecycle_hook}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        lifecycle_transition: builtins.str,
        name: builtins.str,
        default_result: typing.Optional[builtins.str] = None,
        heartbeat_timeout: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        notification_metadata: typing.Optional[builtins.str] = None,
        notification_target_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook aws_autoscaling_lifecycle_hook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#autoscaling_group_name AutoscalingLifecycleHook#autoscaling_group_name}.
        :param lifecycle_transition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#lifecycle_transition AutoscalingLifecycleHook#lifecycle_transition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#name AutoscalingLifecycleHook#name}.
        :param default_result: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#default_result AutoscalingLifecycleHook#default_result}.
        :param heartbeat_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#heartbeat_timeout AutoscalingLifecycleHook#heartbeat_timeout}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#id AutoscalingLifecycleHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_metadata AutoscalingLifecycleHook#notification_metadata}.
        :param notification_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_target_arn AutoscalingLifecycleHook#notification_target_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#role_arn AutoscalingLifecycleHook#role_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingLifecycleHook.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingLifecycleHookConfig(
            autoscaling_group_name=autoscaling_group_name,
            lifecycle_transition=lifecycle_transition,
            name=name,
            default_result=default_result,
            heartbeat_timeout=heartbeat_timeout,
            id=id,
            notification_metadata=notification_metadata,
            notification_target_arn=notification_target_arn,
            role_arn=role_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultResult")
    def reset_default_result(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResult", []))

    @jsii.member(jsii_name="resetHeartbeatTimeout")
    def reset_heartbeat_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeartbeatTimeout", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationMetadata")
    def reset_notification_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationMetadata", []))

    @jsii.member(jsii_name="resetNotificationTargetArn")
    def reset_notification_target_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTargetArn", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResultInput")
    def default_result_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultResultInput"))

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeoutInput")
    def heartbeat_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heartbeatTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransitionInput")
    def lifecycle_transition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationMetadataInput")
    def notification_metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArnInput")
    def notification_target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTargetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "autoscaling_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultResult")
    def default_result(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultResult"))

    @default_result.setter
    def default_result(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "default_result").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultResult", value)

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeout")
    def heartbeat_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "heartbeatTimeout"))

    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "heartbeat_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "heartbeatTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransition")
    def lifecycle_transition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleTransition"))

    @lifecycle_transition.setter
    def lifecycle_transition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "lifecycle_transition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleTransition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationMetadata")
    def notification_metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationMetadata"))

    @notification_metadata.setter
    def notification_metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "notification_metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArn")
    def notification_target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTargetArn"))

    @notification_target_arn.setter
    def notification_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "notification_target_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingLifecycleHook, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingLifecycleHookConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "lifecycle_transition": "lifecycleTransition",
        "name": "name",
        "default_result": "defaultResult",
        "heartbeat_timeout": "heartbeatTimeout",
        "id": "id",
        "notification_metadata": "notificationMetadata",
        "notification_target_arn": "notificationTargetArn",
        "role_arn": "roleArn",
    },
)
class AutoscalingLifecycleHookConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        lifecycle_transition: builtins.str,
        name: builtins.str,
        default_result: typing.Optional[builtins.str] = None,
        heartbeat_timeout: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        notification_metadata: typing.Optional[builtins.str] = None,
        notification_target_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#autoscaling_group_name AutoscalingLifecycleHook#autoscaling_group_name}.
        :param lifecycle_transition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#lifecycle_transition AutoscalingLifecycleHook#lifecycle_transition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#name AutoscalingLifecycleHook#name}.
        :param default_result: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#default_result AutoscalingLifecycleHook#default_result}.
        :param heartbeat_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#heartbeat_timeout AutoscalingLifecycleHook#heartbeat_timeout}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#id AutoscalingLifecycleHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_metadata AutoscalingLifecycleHook#notification_metadata}.
        :param notification_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_target_arn AutoscalingLifecycleHook#notification_target_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#role_arn AutoscalingLifecycleHook#role_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingLifecycleHookConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument lifecycle_transition", value=lifecycle_transition, expected_type=type_hints["lifecycle_transition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_result", value=default_result, expected_type=type_hints["default_result"])
            check_type(argname="argument heartbeat_timeout", value=heartbeat_timeout, expected_type=type_hints["heartbeat_timeout"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_metadata", value=notification_metadata, expected_type=type_hints["notification_metadata"])
            check_type(argname="argument notification_target_arn", value=notification_target_arn, expected_type=type_hints["notification_target_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
            "lifecycle_transition": lifecycle_transition,
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
        if default_result is not None:
            self._values["default_result"] = default_result
        if heartbeat_timeout is not None:
            self._values["heartbeat_timeout"] = heartbeat_timeout
        if id is not None:
            self._values["id"] = id
        if notification_metadata is not None:
            self._values["notification_metadata"] = notification_metadata
        if notification_target_arn is not None:
            self._values["notification_target_arn"] = notification_target_arn
        if role_arn is not None:
            self._values["role_arn"] = role_arn

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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#autoscaling_group_name AutoscalingLifecycleHook#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle_transition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#lifecycle_transition AutoscalingLifecycleHook#lifecycle_transition}.'''
        result = self._values.get("lifecycle_transition")
        assert result is not None, "Required property 'lifecycle_transition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#name AutoscalingLifecycleHook#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_result(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#default_result AutoscalingLifecycleHook#default_result}.'''
        result = self._values.get("default_result")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#heartbeat_timeout AutoscalingLifecycleHook#heartbeat_timeout}.'''
        result = self._values.get("heartbeat_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#id AutoscalingLifecycleHook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_metadata(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_metadata AutoscalingLifecycleHook#notification_metadata}.'''
        result = self._values.get("notification_metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_target_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#notification_target_arn AutoscalingLifecycleHook#notification_target_arn}.'''
        result = self._values.get("notification_target_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook#role_arn AutoscalingLifecycleHook#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingLifecycleHookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingNotification(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingNotification",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification aws_autoscaling_notification}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        group_names: typing.Sequence[builtins.str],
        notifications: typing.Sequence[builtins.str],
        topic_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification aws_autoscaling_notification} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#group_names AutoscalingNotification#group_names}.
        :param notifications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#notifications AutoscalingNotification#notifications}.
        :param topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#topic_arn AutoscalingNotification#topic_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#id AutoscalingNotification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingNotification.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingNotificationConfig(
            group_names=group_names,
            notifications=notifications,
            topic_arn=topic_arn,
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
    @jsii.member(jsii_name="groupNamesInput")
    def group_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicArnInput")
    def topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNames")
    def group_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupNames"))

    @group_names.setter
    def group_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingNotification, "group_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNames", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingNotification, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notifications"))

    @notifications.setter
    def notifications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingNotification, "notifications").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifications", value)

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @topic_arn.setter
    def topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingNotification, "topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingNotificationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_names": "groupNames",
        "notifications": "notifications",
        "topic_arn": "topicArn",
        "id": "id",
    },
)
class AutoscalingNotificationConfig(cdktf.TerraformMetaArguments):
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
        group_names: typing.Sequence[builtins.str],
        notifications: typing.Sequence[builtins.str],
        topic_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#group_names AutoscalingNotification#group_names}.
        :param notifications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#notifications AutoscalingNotification#notifications}.
        :param topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#topic_arn AutoscalingNotification#topic_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#id AutoscalingNotification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingNotificationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_names", value=group_names, expected_type=type_hints["group_names"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_names": group_names,
            "notifications": notifications,
            "topic_arn": topic_arn,
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
    def group_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#group_names AutoscalingNotification#group_names}.'''
        result = self._values.get("group_names")
        assert result is not None, "Required property 'group_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def notifications(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#notifications AutoscalingNotification#notifications}.'''
        result = self._values.get("notifications")
        assert result is not None, "Required property 'notifications' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#topic_arn AutoscalingNotification#topic_arn}.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_notification#id AutoscalingNotification#id}.

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
        return "AutoscalingNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy aws_autoscaling_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        name: builtins.str,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_type: typing.Optional[builtins.str] = None,
        predictive_scaling_configuration: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        scaling_adjustment: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[str, typing.Any]]]]] = None,
        target_tracking_configuration: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy aws_autoscaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.
        :param estimated_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.
        :param predictive_scaling_configuration: predictive_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        :param target_tracking_configuration: target_tracking_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingPolicyConfig(
            autoscaling_group_name=autoscaling_group_name,
            name=name,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            enabled=enabled,
            estimated_instance_warmup=estimated_instance_warmup,
            id=id,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            policy_type=policy_type,
            predictive_scaling_configuration=predictive_scaling_configuration,
            scaling_adjustment=scaling_adjustment,
            step_adjustment=step_adjustment,
            target_tracking_configuration=target_tracking_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPredictiveScalingConfiguration")
    def put_predictive_scaling_configuration(
        self,
        *,
        metric_specification: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", typing.Dict[str, typing.Any]],
        max_capacity_breach_behavior: typing.Optional[builtins.str] = None,
        max_capacity_buffer: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        scheduling_buffer_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_specification: metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        :param max_capacity_breach_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.
        :param max_capacity_buffer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.
        :param scheduling_buffer_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfiguration(
            metric_specification=metric_specification,
            max_capacity_breach_behavior=max_capacity_breach_behavior,
            max_capacity_buffer=max_capacity_buffer,
            mode=mode,
            scheduling_buffer_time=scheduling_buffer_time,
        )

        return typing.cast(None, jsii.invoke(self, "putPredictiveScalingConfiguration", [value]))

    @jsii.member(jsii_name="putStepAdjustment")
    def put_step_adjustment(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicy.put_step_adjustment)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepAdjustment", [value]))

    @jsii.member(jsii_name="putTargetTrackingConfiguration")
    def put_target_tracking_configuration(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        value = AutoscalingPolicyTargetTrackingConfiguration(
            target_value=target_value,
            customized_metric_specification=customized_metric_specification,
            disable_scale_in=disable_scale_in,
            predefined_metric_specification=predefined_metric_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetTrackingConfiguration", [value]))

    @jsii.member(jsii_name="resetAdjustmentType")
    def reset_adjustment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustmentType", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEstimatedInstanceWarmup")
    def reset_estimated_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEstimatedInstanceWarmup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetricAggregationType")
    def reset_metric_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricAggregationType", []))

    @jsii.member(jsii_name="resetMinAdjustmentMagnitude")
    def reset_min_adjustment_magnitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinAdjustmentMagnitude", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @jsii.member(jsii_name="resetPredictiveScalingConfiguration")
    def reset_predictive_scaling_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveScalingConfiguration", []))

    @jsii.member(jsii_name="resetScalingAdjustment")
    def reset_scaling_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingAdjustment", []))

    @jsii.member(jsii_name="resetStepAdjustment")
    def reset_step_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepAdjustment", []))

    @jsii.member(jsii_name="resetTargetTrackingConfiguration")
    def reset_target_tracking_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTrackingConfiguration", []))

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
    @jsii.member(jsii_name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationOutputReference", jsii.get(self, "predictiveScalingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustment")
    def step_adjustment(self) -> "AutoscalingPolicyStepAdjustmentList":
        return typing.cast("AutoscalingPolicyStepAdjustmentList", jsii.get(self, "stepAdjustment"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfiguration")
    def target_tracking_configuration(
        self,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationOutputReference":
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationOutputReference", jsii.get(self, "targetTrackingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentTypeInput")
    def adjustment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmupInput")
    def estimated_instance_warmup_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "estimatedInstanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metricAggregationTypeInput")
    def metric_aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricAggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitudeInput")
    def min_adjustment_magnitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minAdjustmentMagnitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingConfigurationInput")
    def predictive_scaling_configuration_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"], jsii.get(self, "predictiveScalingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustmentInput")
    def scaling_adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scalingAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustmentInput")
    def step_adjustment_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]], jsii.get(self, "stepAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfigurationInput")
    def target_tracking_configuration_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"]:
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"], jsii.get(self, "targetTrackingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentType")
    def adjustment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentType"))

    @adjustment_type.setter
    def adjustment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "adjustment_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentType", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "autoscaling_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "cooldown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "estimatedInstanceWarmup"))

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "estimated_instance_warmup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "estimatedInstanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metricAggregationType")
    def metric_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricAggregationType"))

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "metric_aggregation_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricAggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minAdjustmentMagnitude"))

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "min_adjustment_magnitude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minAdjustmentMagnitude", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "policy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicy, "scaling_adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "name": "name",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "enabled": "enabled",
        "estimated_instance_warmup": "estimatedInstanceWarmup",
        "id": "id",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "policy_type": "policyType",
        "predictive_scaling_configuration": "predictiveScalingConfiguration",
        "scaling_adjustment": "scalingAdjustment",
        "step_adjustment": "stepAdjustment",
        "target_tracking_configuration": "targetTrackingConfiguration",
    },
)
class AutoscalingPolicyConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        name: builtins.str,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_type: typing.Optional[builtins.str] = None,
        predictive_scaling_configuration: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        scaling_adjustment: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[str, typing.Any]]]]] = None,
        target_tracking_configuration: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.
        :param estimated_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.
        :param predictive_scaling_configuration: predictive_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        :param target_tracking_configuration: target_tracking_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(predictive_scaling_configuration, dict):
            predictive_scaling_configuration = AutoscalingPolicyPredictiveScalingConfiguration(**predictive_scaling_configuration)
        if isinstance(target_tracking_configuration, dict):
            target_tracking_configuration = AutoscalingPolicyTargetTrackingConfiguration(**target_tracking_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument estimated_instance_warmup", value=estimated_instance_warmup, expected_type=type_hints["estimated_instance_warmup"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument predictive_scaling_configuration", value=predictive_scaling_configuration, expected_type=type_hints["predictive_scaling_configuration"])
            check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
            check_type(argname="argument step_adjustment", value=step_adjustment, expected_type=type_hints["step_adjustment"])
            check_type(argname="argument target_tracking_configuration", value=target_tracking_configuration, expected_type=type_hints["target_tracking_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
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
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if enabled is not None:
            self._values["enabled"] = enabled
        if estimated_instance_warmup is not None:
            self._values["estimated_instance_warmup"] = estimated_instance_warmup
        if id is not None:
            self._values["id"] = id
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if policy_type is not None:
            self._values["policy_type"] = policy_type
        if predictive_scaling_configuration is not None:
            self._values["predictive_scaling_configuration"] = predictive_scaling_configuration
        if scaling_adjustment is not None:
            self._values["scaling_adjustment"] = scaling_adjustment
        if step_adjustment is not None:
            self._values["step_adjustment"] = step_adjustment
        if target_tracking_configuration is not None:
            self._values["target_tracking_configuration"] = target_tracking_configuration

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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.'''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.'''
        result = self._values.get("estimated_instance_warmup")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.'''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.'''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def predictive_scaling_configuration(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"]:
        '''predictive_scaling_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        '''
        result = self._values.get("predictive_scaling_configuration")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"], result)

    @builtins.property
    def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_adjustment(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]]:
        '''step_adjustment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        '''
        result = self._values.get("step_adjustment")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]], result)

    @builtins.property
    def target_tracking_configuration(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"]:
        '''target_tracking_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        '''
        result = self._values.get("target_tracking_configuration")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "metric_specification": "metricSpecification",
        "max_capacity_breach_behavior": "maxCapacityBreachBehavior",
        "max_capacity_buffer": "maxCapacityBuffer",
        "mode": "mode",
        "scheduling_buffer_time": "schedulingBufferTime",
    },
)
class AutoscalingPolicyPredictiveScalingConfiguration:
    def __init__(
        self,
        *,
        metric_specification: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", typing.Dict[str, typing.Any]],
        max_capacity_breach_behavior: typing.Optional[builtins.str] = None,
        max_capacity_buffer: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        scheduling_buffer_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_specification: metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        :param max_capacity_breach_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.
        :param max_capacity_buffer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.
        :param scheduling_buffer_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.
        '''
        if isinstance(metric_specification, dict):
            metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(**metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfiguration.__init__)
            check_type(argname="argument metric_specification", value=metric_specification, expected_type=type_hints["metric_specification"])
            check_type(argname="argument max_capacity_breach_behavior", value=max_capacity_breach_behavior, expected_type=type_hints["max_capacity_breach_behavior"])
            check_type(argname="argument max_capacity_buffer", value=max_capacity_buffer, expected_type=type_hints["max_capacity_buffer"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument scheduling_buffer_time", value=scheduling_buffer_time, expected_type=type_hints["scheduling_buffer_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_specification": metric_specification,
        }
        if max_capacity_breach_behavior is not None:
            self._values["max_capacity_breach_behavior"] = max_capacity_breach_behavior
        if max_capacity_buffer is not None:
            self._values["max_capacity_buffer"] = max_capacity_buffer
        if mode is not None:
            self._values["mode"] = mode
        if scheduling_buffer_time is not None:
            self._values["scheduling_buffer_time"] = scheduling_buffer_time

    @builtins.property
    def metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification":
        '''metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        '''
        result = self._values.get("metric_specification")
        assert result is not None, "Required property 'metric_specification' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", result)

    @builtins.property
    def max_capacity_breach_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.'''
        result = self._values.get("max_capacity_breach_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity_buffer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.'''
        result = self._values.get("max_capacity_buffer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_buffer_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.'''
        result = self._values.get("scheduling_buffer_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_capacity_metric_specification": "customizedCapacityMetricSpecification",
        "customized_load_metric_specification": "customizedLoadMetricSpecification",
        "customized_scaling_metric_specification": "customizedScalingMetricSpecification",
        "predefined_load_metric_specification": "predefinedLoadMetricSpecification",
        "predefined_metric_pair_specification": "predefinedMetricPairSpecification",
        "predefined_scaling_metric_specification": "predefinedScalingMetricSpecification",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_capacity_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        customized_load_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        customized_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        predefined_load_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        predefined_metric_pair_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification", typing.Dict[str, typing.Any]]] = None,
        predefined_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_capacity_metric_specification: customized_capacity_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        :param customized_load_metric_specification: customized_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        :param customized_scaling_metric_specification: customized_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        :param predefined_load_metric_specification: predefined_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        :param predefined_metric_pair_specification: predefined_metric_pair_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        :param predefined_scaling_metric_specification: predefined_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        if isinstance(customized_capacity_metric_specification, dict):
            customized_capacity_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(**customized_capacity_metric_specification)
        if isinstance(customized_load_metric_specification, dict):
            customized_load_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(**customized_load_metric_specification)
        if isinstance(customized_scaling_metric_specification, dict):
            customized_scaling_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(**customized_scaling_metric_specification)
        if isinstance(predefined_load_metric_specification, dict):
            predefined_load_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(**predefined_load_metric_specification)
        if isinstance(predefined_metric_pair_specification, dict):
            predefined_metric_pair_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(**predefined_metric_pair_specification)
        if isinstance(predefined_scaling_metric_specification, dict):
            predefined_scaling_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(**predefined_scaling_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification.__init__)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_capacity_metric_specification", value=customized_capacity_metric_specification, expected_type=type_hints["customized_capacity_metric_specification"])
            check_type(argname="argument customized_load_metric_specification", value=customized_load_metric_specification, expected_type=type_hints["customized_load_metric_specification"])
            check_type(argname="argument customized_scaling_metric_specification", value=customized_scaling_metric_specification, expected_type=type_hints["customized_scaling_metric_specification"])
            check_type(argname="argument predefined_load_metric_specification", value=predefined_load_metric_specification, expected_type=type_hints["predefined_load_metric_specification"])
            check_type(argname="argument predefined_metric_pair_specification", value=predefined_metric_pair_specification, expected_type=type_hints["predefined_metric_pair_specification"])
            check_type(argname="argument predefined_scaling_metric_specification", value=predefined_scaling_metric_specification, expected_type=type_hints["predefined_scaling_metric_specification"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_capacity_metric_specification is not None:
            self._values["customized_capacity_metric_specification"] = customized_capacity_metric_specification
        if customized_load_metric_specification is not None:
            self._values["customized_load_metric_specification"] = customized_load_metric_specification
        if customized_scaling_metric_specification is not None:
            self._values["customized_scaling_metric_specification"] = customized_scaling_metric_specification
        if predefined_load_metric_specification is not None:
            self._values["predefined_load_metric_specification"] = predefined_load_metric_specification
        if predefined_metric_pair_specification is not None:
            self._values["predefined_metric_pair_specification"] = predefined_metric_pair_specification
        if predefined_scaling_metric_specification is not None:
            self._values["predefined_scaling_metric_specification"] = predefined_scaling_metric_specification

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_capacity_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification"]:
        '''customized_capacity_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        '''
        result = self._values.get("customized_capacity_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification"], result)

    @builtins.property
    def customized_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification"]:
        '''customized_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        '''
        result = self._values.get("customized_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification"], result)

    @builtins.property
    def customized_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification"]:
        '''customized_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        '''
        result = self._values.get("customized_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification"], result)

    @builtins.property
    def predefined_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"]:
        '''predefined_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        '''
        result = self._values.get("predefined_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"], result)

    @builtins.property
    def predefined_metric_pair_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"]:
        '''predefined_metric_pair_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        '''
        result = self._values.get("predefined_metric_pair_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"], result)

    @builtins.property
    def predefined_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"]:
        '''predefined_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        result = self._values.get("predefined_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification.__init__)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat.__init__)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference, "stat").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference, "return_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference.put_metric_data_queries)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification.__init__)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat.__init__)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference, "stat").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference, "return_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference.put_metric_data_queries)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification.__init__)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat.__init__)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference.put_dimensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference, "stat").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference, "return_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference.put_metric_data_queries)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomizedCapacityMetricSpecification")
    def put_customized_capacity_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedCapacityMetricSpecification", [value]))

    @jsii.member(jsii_name="putCustomizedLoadMetricSpecification")
    def put_customized_load_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putCustomizedScalingMetricSpecification")
    def put_customized_scaling_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedLoadMetricSpecification")
    def put_predefined_load_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedMetricPairSpecification")
    def put_predefined_metric_pair_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedMetricPairSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedScalingMetricSpecification")
    def put_predefined_scaling_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedCapacityMetricSpecification")
    def reset_customized_capacity_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedCapacityMetricSpecification", []))

    @jsii.member(jsii_name="resetCustomizedLoadMetricSpecification")
    def reset_customized_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetCustomizedScalingMetricSpecification")
    def reset_customized_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedScalingMetricSpecification", []))

    @jsii.member(jsii_name="resetPredefinedLoadMetricSpecification")
    def reset_predefined_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetPredefinedMetricPairSpecification")
    def reset_predefined_metric_pair_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedMetricPairSpecification", []))

    @jsii.member(jsii_name="resetPredefinedScalingMetricSpecification")
    def reset_predefined_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedScalingMetricSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference, jsii.get(self, "customizedCapacityMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference, jsii.get(self, "customizedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference, jsii.get(self, "customizedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference", jsii.get(self, "predefinedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference", jsii.get(self, "predefinedMetricPairSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference", jsii.get(self, "predefinedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedCapacityMetricSpecificationInput")
    def customized_capacity_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification], jsii.get(self, "customizedCapacityMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecificationInput")
    def customized_load_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification], jsii.get(self, "customizedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecificationInput")
    def customized_scaling_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification], jsii.get(self, "customizedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecificationInput")
    def predefined_load_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"], jsii.get(self, "predefinedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricPairSpecificationInput")
    def predefined_metric_pair_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"], jsii.get(self, "predefinedMetricPairSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecificationInput")
    def predefined_scaling_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"], jsii.get(self, "predefinedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValueInput")
    def target_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetValueInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference, "target_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification.__init__)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference, "predefined_metric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference, "resource_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification.__init__)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference, "predefined_metric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference, "resource_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification.__init__)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference, "predefined_metric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference, "resource_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyPredictiveScalingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyPredictiveScalingConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricSpecification")
    def put_metric_specification(
        self,
        *,
        target_value: jsii.Number,
        customized_capacity_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification, typing.Dict[str, typing.Any]]] = None,
        customized_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification, typing.Dict[str, typing.Any]]] = None,
        customized_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification, typing.Dict[str, typing.Any]]] = None,
        predefined_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification, typing.Dict[str, typing.Any]]] = None,
        predefined_metric_pair_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification, typing.Dict[str, typing.Any]]] = None,
        predefined_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_capacity_metric_specification: customized_capacity_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        :param customized_load_metric_specification: customized_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        :param customized_scaling_metric_specification: customized_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        :param predefined_load_metric_specification: predefined_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        :param predefined_metric_pair_specification: predefined_metric_pair_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        :param predefined_scaling_metric_specification: predefined_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(
            target_value=target_value,
            customized_capacity_metric_specification=customized_capacity_metric_specification,
            customized_load_metric_specification=customized_load_metric_specification,
            customized_scaling_metric_specification=customized_scaling_metric_specification,
            predefined_load_metric_specification=predefined_load_metric_specification,
            predefined_metric_pair_specification=predefined_metric_pair_specification,
            predefined_scaling_metric_specification=predefined_scaling_metric_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putMetricSpecification", [value]))

    @jsii.member(jsii_name="resetMaxCapacityBreachBehavior")
    def reset_max_capacity_breach_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacityBreachBehavior", []))

    @jsii.member(jsii_name="resetMaxCapacityBuffer")
    def reset_max_capacity_buffer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacityBuffer", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSchedulingBufferTime")
    def reset_scheduling_buffer_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingBufferTime", []))

    @builtins.property
    @jsii.member(jsii_name="metricSpecification")
    def metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference, jsii.get(self, "metricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBreachBehaviorInput")
    def max_capacity_breach_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityBreachBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBufferInput")
    def max_capacity_buffer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityBufferInput"))

    @builtins.property
    @jsii.member(jsii_name="metricSpecificationInput")
    def metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification], jsii.get(self, "metricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingBufferTimeInput")
    def scheduling_buffer_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingBufferTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBreachBehavior")
    def max_capacity_breach_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacityBreachBehavior"))

    @max_capacity_breach_behavior.setter
    def max_capacity_breach_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationOutputReference, "max_capacity_breach_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacityBreachBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBuffer")
    def max_capacity_buffer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacityBuffer"))

    @max_capacity_buffer.setter
    def max_capacity_buffer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationOutputReference, "max_capacity_buffer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacityBuffer", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingBufferTime"))

    @scheduling_buffer_time.setter
    def scheduling_buffer_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationOutputReference, "scheduling_buffer_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingBufferTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyPredictiveScalingConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyStepAdjustment",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_adjustment": "scalingAdjustment",
        "metric_interval_lower_bound": "metricIntervalLowerBound",
        "metric_interval_upper_bound": "metricIntervalUpperBound",
    },
)
class AutoscalingPolicyStepAdjustment:
    def __init__(
        self,
        *,
        scaling_adjustment: jsii.Number,
        metric_interval_lower_bound: typing.Optional[builtins.str] = None,
        metric_interval_upper_bound: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param metric_interval_lower_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_lower_bound AutoscalingPolicy#metric_interval_lower_bound}.
        :param metric_interval_upper_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_upper_bound AutoscalingPolicy#metric_interval_upper_bound}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyStepAdjustment.__init__)
            check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
            check_type(argname="argument metric_interval_lower_bound", value=metric_interval_lower_bound, expected_type=type_hints["metric_interval_lower_bound"])
            check_type(argname="argument metric_interval_upper_bound", value=metric_interval_upper_bound, expected_type=type_hints["metric_interval_upper_bound"])
        self._values: typing.Dict[str, typing.Any] = {
            "scaling_adjustment": scaling_adjustment,
        }
        if metric_interval_lower_bound is not None:
            self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
        if metric_interval_upper_bound is not None:
            self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

    @builtins.property
    def scaling_adjustment(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        assert result is not None, "Required property 'scaling_adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_interval_lower_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_lower_bound AutoscalingPolicy#metric_interval_lower_bound}.'''
        result = self._values.get("metric_interval_lower_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_interval_upper_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_upper_bound AutoscalingPolicy#metric_interval_upper_bound}.'''
        result = self._values.get("metric_interval_upper_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyStepAdjustment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyStepAdjustmentList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyStepAdjustmentList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyStepAdjustmentList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyStepAdjustmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyStepAdjustmentList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyStepAdjustmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyStepAdjustmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyStepAdjustmentOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyStepAdjustmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMetricIntervalLowerBound")
    def reset_metric_interval_lower_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalLowerBound", []))

    @jsii.member(jsii_name="resetMetricIntervalUpperBound")
    def reset_metric_interval_upper_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalUpperBound", []))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBoundInput")
    def metric_interval_lower_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalLowerBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBoundInput")
    def metric_interval_upper_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalUpperBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustmentInput")
    def scaling_adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scalingAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalLowerBound"))

    @metric_interval_lower_bound.setter
    def metric_interval_lower_bound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentOutputReference, "metric_interval_lower_bound").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalLowerBound", value)

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalUpperBound"))

    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentOutputReference, "metric_interval_upper_bound").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalUpperBound", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentOutputReference, "scaling_adjustment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyStepAdjustmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_metric_specification": "customizedMetricSpecification",
        "disable_scale_in": "disableScaleIn",
        "predefined_metric_specification": "predefinedMetricSpecification",
    },
)
class AutoscalingPolicyTargetTrackingConfiguration:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        if isinstance(customized_metric_specification, dict):
            customized_metric_specification = AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(**customized_metric_specification)
        if isinstance(predefined_metric_specification, dict):
            predefined_metric_specification = AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(**predefined_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfiguration.__init__)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_metric_specification", value=customized_metric_specification, expected_type=type_hints["customized_metric_specification"])
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument predefined_metric_specification", value=predefined_metric_specification, expected_type=type_hints["predefined_metric_specification"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_metric_specification is not None:
            self._values["customized_metric_specification"] = customized_metric_specification
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if predefined_metric_specification is not None:
            self._values["predefined_metric_specification"] = predefined_metric_specification

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification"]:
        '''customized_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        '''
        result = self._values.get("customized_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification"], result)

    @builtins.property
    def disable_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.'''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def predefined_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"]:
        '''predefined_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        result = self._values.get("predefined_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "metric_dimension": "metricDimension",
        "unit": "unit",
    },
)
class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        metric_dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension", typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.
        :param metric_dimension: metric_dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "statistic": statistic,
        }
        if metric_dimension is not None:
            self._values["metric_dimension"] = metric_dimension
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_dimension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension"]]]:
        '''metric_dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        '''
        result = self._values.get("metric_dimension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension"]]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDimension")
    def put_metric_dimension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference.put_metric_dimension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDimension", [value]))

    @jsii.member(jsii_name="resetMetricDimension")
    def reset_metric_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricDimension", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metricDimension")
    def metric_dimension(
        self,
    ) -> AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList:
        return typing.cast(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, jsii.get(self, "metricDimension"))

    @builtins.property
    @jsii.member(jsii_name="metricDimensionInput")
    def metric_dimension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]], jsii.get(self, "metricDimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, "statistic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomizedMetricSpecification")
    def put_customized_metric_specification(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        metric_dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.
        :param metric_dimension: metric_dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            metric_dimension=metric_dimension,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedMetricSpecification")
    def put_predefined_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedMetricSpecification")
    def reset_customized_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedMetricSpecification", []))

    @jsii.member(jsii_name="resetDisableScaleIn")
    def reset_disable_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableScaleIn", []))

    @jsii.member(jsii_name="resetPredefinedMetricSpecification")
    def reset_predefined_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedMetricSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, jsii.get(self, "customizedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference", jsii.get(self, "predefinedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecificationInput")
    def customized_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification], jsii.get(self, "customizedMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleInInput")
    def disable_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecificationInput")
    def predefined_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"], jsii.get(self, "predefinedMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValueInput")
    def target_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetValueInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleIn")
    def disable_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableScaleIn"))

    @disable_scale_in.setter
    def disable_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationOutputReference, "disable_scale_in").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationOutputReference, "target_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfiguration]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification.__init__)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResourceLabel")
    def reset_resource_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabel", []))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference, "predefined_metric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference, "resource_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingSchedule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingSchedule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule aws_autoscaling_schedule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        scheduled_action_name: builtins.str,
        desired_capacity: typing.Optional[jsii.Number] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        recurrence: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule aws_autoscaling_schedule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#autoscaling_group_name AutoscalingSchedule#autoscaling_group_name}.
        :param scheduled_action_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#scheduled_action_name AutoscalingSchedule#scheduled_action_name}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#desired_capacity AutoscalingSchedule#desired_capacity}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#end_time AutoscalingSchedule#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#id AutoscalingSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#max_size AutoscalingSchedule#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#min_size AutoscalingSchedule#min_size}.
        :param recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#recurrence AutoscalingSchedule#recurrence}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#start_time AutoscalingSchedule#start_time}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#time_zone AutoscalingSchedule#time_zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingSchedule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingScheduleConfig(
            autoscaling_group_name=autoscaling_group_name,
            scheduled_action_name=scheduled_action_name,
            desired_capacity=desired_capacity,
            end_time=end_time,
            id=id,
            max_size=max_size,
            min_size=min_size,
            recurrence=recurrence,
            start_time=start_time,
            time_zone=time_zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxSize")
    def reset_max_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSize", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetRecurrence")
    def reset_recurrence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurrence", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

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
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrenceInput")
    def recurrence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledActionNameInput")
    def scheduled_action_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledActionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "autoscaling_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "desired_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "max_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "min_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrence"))

    @recurrence.setter
    def recurrence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "recurrence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrence", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledActionName")
    def scheduled_action_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduledActionName"))

    @scheduled_action_name.setter
    def scheduled_action_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "scheduled_action_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionName", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutoscalingSchedule, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.AutoscalingScheduleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "scheduled_action_name": "scheduledActionName",
        "desired_capacity": "desiredCapacity",
        "end_time": "endTime",
        "id": "id",
        "max_size": "maxSize",
        "min_size": "minSize",
        "recurrence": "recurrence",
        "start_time": "startTime",
        "time_zone": "timeZone",
    },
)
class AutoscalingScheduleConfig(cdktf.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        scheduled_action_name: builtins.str,
        desired_capacity: typing.Optional[jsii.Number] = None,
        end_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        recurrence: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#autoscaling_group_name AutoscalingSchedule#autoscaling_group_name}.
        :param scheduled_action_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#scheduled_action_name AutoscalingSchedule#scheduled_action_name}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#desired_capacity AutoscalingSchedule#desired_capacity}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#end_time AutoscalingSchedule#end_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#id AutoscalingSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#max_size AutoscalingSchedule#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#min_size AutoscalingSchedule#min_size}.
        :param recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#recurrence AutoscalingSchedule#recurrence}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#start_time AutoscalingSchedule#start_time}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#time_zone AutoscalingSchedule#time_zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AutoscalingScheduleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument recurrence", value=recurrence, expected_type=type_hints["recurrence"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
            "scheduled_action_name": scheduled_action_name,
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
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if end_time is not None:
            self._values["end_time"] = end_time
        if id is not None:
            self._values["id"] = id
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if recurrence is not None:
            self._values["recurrence"] = recurrence
        if start_time is not None:
            self._values["start_time"] = start_time
        if time_zone is not None:
            self._values["time_zone"] = time_zone

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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#autoscaling_group_name AutoscalingSchedule#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_action_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#scheduled_action_name AutoscalingSchedule#scheduled_action_name}.'''
        result = self._values.get("scheduled_action_name")
        assert result is not None, "Required property 'scheduled_action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#desired_capacity AutoscalingSchedule#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#end_time AutoscalingSchedule#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#id AutoscalingSchedule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#max_size AutoscalingSchedule#max_size}.'''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#min_size AutoscalingSchedule#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def recurrence(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#recurrence AutoscalingSchedule#recurrence}.'''
        result = self._values.get("recurrence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#start_time AutoscalingSchedule#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule#time_zone AutoscalingSchedule#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingScheduleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsAutoscalingGroup(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group aws_autoscaling_group}.'''

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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group aws_autoscaling_group} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#name DataAwsAutoscalingGroup#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#id DataAwsAutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsAutoscalingGroupConfig(
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
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @builtins.property
    @jsii.member(jsii_name="defaultCooldown")
    def default_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultCooldown"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @builtins.property
    @jsii.member(jsii_name="enabledMetrics")
    def enabled_metrics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledMetrics"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriod"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @builtins.property
    @jsii.member(jsii_name="launchConfiguration")
    def launch_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> "DataAwsAutoscalingGroupLaunchTemplateList":
        return typing.cast("DataAwsAutoscalingGroupLaunchTemplateList", jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancers"))

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @builtins.property
    @jsii.member(jsii_name="newInstancesProtectedFromScaleIn")
    def new_instances_protected_from_scale_in(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "newInstancesProtectedFromScaleIn"))

    @builtins.property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementGroup"))

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceLinkedRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArns")
    def target_group_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetGroupArns"))

    @builtins.property
    @jsii.member(jsii_name="terminationPolicies")
    def termination_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "terminationPolicies"))

    @builtins.property
    @jsii.member(jsii_name="vpcZoneIdentifier")
    def vpc_zone_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcZoneIdentifier"))

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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroup, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupConfig",
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
class DataAwsAutoscalingGroupConfig(cdktf.TerraformMetaArguments):
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
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#name DataAwsAutoscalingGroup#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#id DataAwsAutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupConfig.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#name DataAwsAutoscalingGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_group#id DataAwsAutoscalingGroup#id}.

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
        return "DataAwsAutoscalingGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsAutoscalingGroupLaunchTemplate:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsAutoscalingGroupLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsAutoscalingGroupLaunchTemplateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupLaunchTemplateList",
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
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupLaunchTemplateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsAutoscalingGroupLaunchTemplateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupLaunchTemplateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsAutoscalingGroupLaunchTemplateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupLaunchTemplateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupLaunchTemplateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupLaunchTemplateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAwsAutoscalingGroupLaunchTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupLaunchTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsAutoscalingGroupLaunchTemplate]:
        return typing.cast(typing.Optional[DataAwsAutoscalingGroupLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsAutoscalingGroupLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupLaunchTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsAutoscalingGroups(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroups",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups aws_autoscaling_groups}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsAutoscalingGroupsFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups aws_autoscaling_groups} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#filter DataAwsAutoscalingGroups#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#id DataAwsAutoscalingGroups#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#names DataAwsAutoscalingGroups#names}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroups.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsAutoscalingGroupsConfig(
            filter=filter,
            id=id,
            names=names,
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsAutoscalingGroupsFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroups.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNames")
    def reset_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNames", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsAutoscalingGroupsFilterList":
        return typing.cast("DataAwsAutoscalingGroupsFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsAutoscalingGroupsFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsAutoscalingGroupsFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namesInput")
    def names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "namesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroups, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="names")
    def names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "names"))

    @names.setter
    def names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroups, "names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "names", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupsConfig",
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
        "names": "names",
    },
)
class DataAwsAutoscalingGroupsConfig(cdktf.TerraformMetaArguments):
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
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsAutoscalingGroupsFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''AWS Auto Scaling.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#filter DataAwsAutoscalingGroups#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#id DataAwsAutoscalingGroups#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#names DataAwsAutoscalingGroups#names}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument names", value=names, expected_type=type_hints["names"])
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
        if names is not None:
            self._values["names"] = names

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsAutoscalingGroupsFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#filter DataAwsAutoscalingGroups#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsAutoscalingGroupsFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#id DataAwsAutoscalingGroups#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#names DataAwsAutoscalingGroups#names}.'''
        result = self._values.get("names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsAutoscalingGroupsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupsFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class DataAwsAutoscalingGroupsFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#name DataAwsAutoscalingGroups#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#values DataAwsAutoscalingGroups#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupsFilter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#name DataAwsAutoscalingGroups#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/autoscaling_groups#values DataAwsAutoscalingGroups#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsAutoscalingGroupsFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsAutoscalingGroupsFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupsFilterList",
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
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupsFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsAutoscalingGroupsFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupsFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsAutoscalingGroupsFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsAutoscalingGroupsFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsAutoscalingGroupsFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsAutoscalingGroupsFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsAutoscalingGroupsFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscaling.DataAwsAutoscalingGroupsFilterOutputReference",
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
            type_hints = typing.get_type_hints(DataAwsAutoscalingGroupsFilterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsAutoscalingGroupsFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsAutoscalingGroupsFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsAutoscalingGroupsFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAwsAutoscalingGroupsFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AutoscalingAttachment",
    "AutoscalingAttachmentConfig",
    "AutoscalingGroup",
    "AutoscalingGroupConfig",
    "AutoscalingGroupInitialLifecycleHook",
    "AutoscalingGroupInitialLifecycleHookList",
    "AutoscalingGroupInitialLifecycleHookOutputReference",
    "AutoscalingGroupInstanceRefresh",
    "AutoscalingGroupInstanceRefreshOutputReference",
    "AutoscalingGroupInstanceRefreshPreferences",
    "AutoscalingGroupInstanceRefreshPreferencesOutputReference",
    "AutoscalingGroupLaunchTemplate",
    "AutoscalingGroupLaunchTemplateOutputReference",
    "AutoscalingGroupMixedInstancesPolicy",
    "AutoscalingGroupMixedInstancesPolicyInstancesDistribution",
    "AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplate",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference",
    "AutoscalingGroupMixedInstancesPolicyOutputReference",
    "AutoscalingGroupTag",
    "AutoscalingGroupTagA",
    "AutoscalingGroupTagAConfig",
    "AutoscalingGroupTagList",
    "AutoscalingGroupTagOutputReference",
    "AutoscalingGroupTagTag",
    "AutoscalingGroupTagTagOutputReference",
    "AutoscalingGroupTimeouts",
    "AutoscalingGroupTimeoutsOutputReference",
    "AutoscalingGroupWarmPool",
    "AutoscalingGroupWarmPoolInstanceReusePolicy",
    "AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference",
    "AutoscalingGroupWarmPoolOutputReference",
    "AutoscalingLifecycleHook",
    "AutoscalingLifecycleHookConfig",
    "AutoscalingNotification",
    "AutoscalingNotificationConfig",
    "AutoscalingPolicy",
    "AutoscalingPolicyConfig",
    "AutoscalingPolicyPredictiveScalingConfiguration",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationOutputReference",
    "AutoscalingPolicyStepAdjustment",
    "AutoscalingPolicyStepAdjustmentList",
    "AutoscalingPolicyStepAdjustmentOutputReference",
    "AutoscalingPolicyTargetTrackingConfiguration",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification",
    "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference",
    "AutoscalingSchedule",
    "AutoscalingScheduleConfig",
    "DataAwsAutoscalingGroup",
    "DataAwsAutoscalingGroupConfig",
    "DataAwsAutoscalingGroupLaunchTemplate",
    "DataAwsAutoscalingGroupLaunchTemplateList",
    "DataAwsAutoscalingGroupLaunchTemplateOutputReference",
    "DataAwsAutoscalingGroups",
    "DataAwsAutoscalingGroupsConfig",
    "DataAwsAutoscalingGroupsFilter",
    "DataAwsAutoscalingGroupsFilterList",
    "DataAwsAutoscalingGroupsFilterOutputReference",
]

publication.publish()
