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


class ElastictranscoderPipeline(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipeline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline aws_elastictranscoder_pipeline}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        input_bucket: builtins.str,
        role: builtins.str,
        aws_kms_key_arn: typing.Optional[builtins.str] = None,
        content_config: typing.Optional[typing.Union["ElastictranscoderPipelineContentConfig", typing.Dict[str, typing.Any]]] = None,
        content_config_permissions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Union["ElastictranscoderPipelineNotifications", typing.Dict[str, typing.Any]]] = None,
        output_bucket: typing.Optional[builtins.str] = None,
        thumbnail_config: typing.Optional[typing.Union["ElastictranscoderPipelineThumbnailConfig", typing.Dict[str, typing.Any]]] = None,
        thumbnail_config_permissions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline aws_elastictranscoder_pipeline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param input_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.
        :param aws_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.
        :param content_config: content_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        :param content_config_permissions: content_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        :param output_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.
        :param thumbnail_config: thumbnail_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        :param thumbnail_config_permissions: thumbnail_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipeline.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastictranscoderPipelineConfig(
            input_bucket=input_bucket,
            role=role,
            aws_kms_key_arn=aws_kms_key_arn,
            content_config=content_config,
            content_config_permissions=content_config_permissions,
            id=id,
            name=name,
            notifications=notifications,
            output_bucket=output_bucket,
            thumbnail_config=thumbnail_config,
            thumbnail_config_permissions=thumbnail_config_permissions,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putContentConfig")
    def put_content_config(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        value = ElastictranscoderPipelineContentConfig(
            bucket=bucket, storage_class=storage_class
        )

        return typing.cast(None, jsii.invoke(self, "putContentConfig", [value]))

    @jsii.member(jsii_name="putContentConfigPermissions")
    def put_content_config_permissions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipeline.put_content_config_permissions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContentConfigPermissions", [value]))

    @jsii.member(jsii_name="putNotifications")
    def put_notifications(
        self,
        *,
        completed: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        progressing: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param completed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.
        :param error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.
        :param progressing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.
        :param warning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.
        '''
        value = ElastictranscoderPipelineNotifications(
            completed=completed, error=error, progressing=progressing, warning=warning
        )

        return typing.cast(None, jsii.invoke(self, "putNotifications", [value]))

    @jsii.member(jsii_name="putThumbnailConfig")
    def put_thumbnail_config(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        value = ElastictranscoderPipelineThumbnailConfig(
            bucket=bucket, storage_class=storage_class
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnailConfig", [value]))

    @jsii.member(jsii_name="putThumbnailConfigPermissions")
    def put_thumbnail_config_permissions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipeline.put_thumbnail_config_permissions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThumbnailConfigPermissions", [value]))

    @jsii.member(jsii_name="resetAwsKmsKeyArn")
    def reset_aws_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsKmsKeyArn", []))

    @jsii.member(jsii_name="resetContentConfig")
    def reset_content_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentConfig", []))

    @jsii.member(jsii_name="resetContentConfigPermissions")
    def reset_content_config_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentConfigPermissions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNotifications")
    def reset_notifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifications", []))

    @jsii.member(jsii_name="resetOutputBucket")
    def reset_output_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputBucket", []))

    @jsii.member(jsii_name="resetThumbnailConfig")
    def reset_thumbnail_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnailConfig", []))

    @jsii.member(jsii_name="resetThumbnailConfigPermissions")
    def reset_thumbnail_config_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnailConfigPermissions", []))

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
    @jsii.member(jsii_name="contentConfig")
    def content_config(self) -> "ElastictranscoderPipelineContentConfigOutputReference":
        return typing.cast("ElastictranscoderPipelineContentConfigOutputReference", jsii.get(self, "contentConfig"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigPermissions")
    def content_config_permissions(
        self,
    ) -> "ElastictranscoderPipelineContentConfigPermissionsList":
        return typing.cast("ElastictranscoderPipelineContentConfigPermissionsList", jsii.get(self, "contentConfigPermissions"))

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> "ElastictranscoderPipelineNotificationsOutputReference":
        return typing.cast("ElastictranscoderPipelineNotificationsOutputReference", jsii.get(self, "notifications"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfig")
    def thumbnail_config(
        self,
    ) -> "ElastictranscoderPipelineThumbnailConfigOutputReference":
        return typing.cast("ElastictranscoderPipelineThumbnailConfigOutputReference", jsii.get(self, "thumbnailConfig"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigPermissions")
    def thumbnail_config_permissions(
        self,
    ) -> "ElastictranscoderPipelineThumbnailConfigPermissionsList":
        return typing.cast("ElastictranscoderPipelineThumbnailConfigPermissionsList", jsii.get(self, "thumbnailConfigPermissions"))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyArnInput")
    def aws_kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsKmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigInput")
    def content_config_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineContentConfig"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineContentConfig"], jsii.get(self, "contentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="contentConfigPermissionsInput")
    def content_config_permissions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]], jsii.get(self, "contentConfigPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputBucketInput")
    def input_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineNotifications"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineNotifications"], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputBucketInput")
    def output_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigInput")
    def thumbnail_config_input(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineThumbnailConfig"]:
        return typing.cast(typing.Optional["ElastictranscoderPipelineThumbnailConfig"], jsii.get(self, "thumbnailConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfigPermissionsInput")
    def thumbnail_config_permissions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]], jsii.get(self, "thumbnailConfigPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyArn")
    def aws_kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsKmsKeyArn"))

    @aws_kms_key_arn.setter
    def aws_kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "aws_kms_key_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsKmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inputBucket")
    def input_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputBucket"))

    @input_bucket.setter
    def input_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "input_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputBucket", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outputBucket")
    def output_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputBucket"))

    @output_bucket.setter
    def output_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "output_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputBucket", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipeline, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "input_bucket": "inputBucket",
        "role": "role",
        "aws_kms_key_arn": "awsKmsKeyArn",
        "content_config": "contentConfig",
        "content_config_permissions": "contentConfigPermissions",
        "id": "id",
        "name": "name",
        "notifications": "notifications",
        "output_bucket": "outputBucket",
        "thumbnail_config": "thumbnailConfig",
        "thumbnail_config_permissions": "thumbnailConfigPermissions",
    },
)
class ElastictranscoderPipelineConfig(cdktf.TerraformMetaArguments):
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
        input_bucket: builtins.str,
        role: builtins.str,
        aws_kms_key_arn: typing.Optional[builtins.str] = None,
        content_config: typing.Optional[typing.Union["ElastictranscoderPipelineContentConfig", typing.Dict[str, typing.Any]]] = None,
        content_config_permissions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineContentConfigPermissions", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Union["ElastictranscoderPipelineNotifications", typing.Dict[str, typing.Any]]] = None,
        output_bucket: typing.Optional[builtins.str] = None,
        thumbnail_config: typing.Optional[typing.Union["ElastictranscoderPipelineThumbnailConfig", typing.Dict[str, typing.Any]]] = None,
        thumbnail_config_permissions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPipelineThumbnailConfigPermissions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''AWS Elastic Transcoder.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param input_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.
        :param aws_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.
        :param content_config: content_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        :param content_config_permissions: content_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.
        :param notifications: notifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        :param output_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.
        :param thumbnail_config: thumbnail_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        :param thumbnail_config_permissions: thumbnail_config_permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(content_config, dict):
            content_config = ElastictranscoderPipelineContentConfig(**content_config)
        if isinstance(notifications, dict):
            notifications = ElastictranscoderPipelineNotifications(**notifications)
        if isinstance(thumbnail_config, dict):
            thumbnail_config = ElastictranscoderPipelineThumbnailConfig(**thumbnail_config)
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument input_bucket", value=input_bucket, expected_type=type_hints["input_bucket"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument aws_kms_key_arn", value=aws_kms_key_arn, expected_type=type_hints["aws_kms_key_arn"])
            check_type(argname="argument content_config", value=content_config, expected_type=type_hints["content_config"])
            check_type(argname="argument content_config_permissions", value=content_config_permissions, expected_type=type_hints["content_config_permissions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
            check_type(argname="argument output_bucket", value=output_bucket, expected_type=type_hints["output_bucket"])
            check_type(argname="argument thumbnail_config", value=thumbnail_config, expected_type=type_hints["thumbnail_config"])
            check_type(argname="argument thumbnail_config_permissions", value=thumbnail_config_permissions, expected_type=type_hints["thumbnail_config_permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "input_bucket": input_bucket,
            "role": role,
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
        if aws_kms_key_arn is not None:
            self._values["aws_kms_key_arn"] = aws_kms_key_arn
        if content_config is not None:
            self._values["content_config"] = content_config
        if content_config_permissions is not None:
            self._values["content_config_permissions"] = content_config_permissions
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if notifications is not None:
            self._values["notifications"] = notifications
        if output_bucket is not None:
            self._values["output_bucket"] = output_bucket
        if thumbnail_config is not None:
            self._values["thumbnail_config"] = thumbnail_config
        if thumbnail_config_permissions is not None:
            self._values["thumbnail_config_permissions"] = thumbnail_config_permissions

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
    def input_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#input_bucket ElastictranscoderPipeline#input_bucket}.'''
        result = self._values.get("input_bucket")
        assert result is not None, "Required property 'input_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#role ElastictranscoderPipeline#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#aws_kms_key_arn ElastictranscoderPipeline#aws_kms_key_arn}.'''
        result = self._values.get("aws_kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_config(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineContentConfig"]:
        '''content_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config ElastictranscoderPipeline#content_config}
        '''
        result = self._values.get("content_config")
        return typing.cast(typing.Optional["ElastictranscoderPipelineContentConfig"], result)

    @builtins.property
    def content_config_permissions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]]:
        '''content_config_permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#content_config_permissions ElastictranscoderPipeline#content_config_permissions}
        '''
        result = self._values.get("content_config_permissions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineContentConfigPermissions"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#id ElastictranscoderPipeline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#name ElastictranscoderPipeline#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineNotifications"]:
        '''notifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#notifications ElastictranscoderPipeline#notifications}
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional["ElastictranscoderPipelineNotifications"], result)

    @builtins.property
    def output_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#output_bucket ElastictranscoderPipeline#output_bucket}.'''
        result = self._values.get("output_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbnail_config(
        self,
    ) -> typing.Optional["ElastictranscoderPipelineThumbnailConfig"]:
        '''thumbnail_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config ElastictranscoderPipeline#thumbnail_config}
        '''
        result = self._values.get("thumbnail_config")
        return typing.cast(typing.Optional["ElastictranscoderPipelineThumbnailConfig"], result)

    @builtins.property
    def thumbnail_config_permissions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]]:
        '''thumbnail_config_permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#thumbnail_config_permissions ElastictranscoderPipeline#thumbnail_config_permissions}
        '''
        result = self._values.get("thumbnail_config_permissions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPipelineThumbnailConfigPermissions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineContentConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "storage_class": "storageClass"},
)
class ElastictranscoderPipelineContentConfig:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfig.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineContentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineContentConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineContentConfigOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigOutputReference, "storage_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPipelineContentConfig]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineContentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineContentConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineContentConfigPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "grantee": "grantee",
        "grantee_type": "granteeType",
    },
)
class ElastictranscoderPipelineContentConfigPermissions:
    def __init__(
        self,
        *,
        access: typing.Optional[typing.Sequence[builtins.str]] = None,
        grantee: typing.Optional[builtins.str] = None,
        grantee_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.
        :param grantee: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.
        :param grantee_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfigPermissions.__init__)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument grantee_type", value=grantee_type, expected_type=type_hints["grantee_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access is not None:
            self._values["access"] = access
        if grantee is not None:
            self._values["grantee"] = grantee
        if grantee_type is not None:
            self._values["grantee_type"] = grantee_type

    @builtins.property
    def access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.'''
        result = self._values.get("access")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grantee(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.'''
        result = self._values.get("grantee")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grantee_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.'''
        result = self._values.get("grantee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineContentConfigPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineContentConfigPermissionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineContentConfigPermissionsList",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfigPermissionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPipelineContentConfigPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfigPermissionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPipelineContentConfigPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineContentConfigPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPipelineContentConfigPermissionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineContentConfigPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineContentConfigPermissionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetGrantee")
    def reset_grantee(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantee", []))

    @jsii.member(jsii_name="resetGranteeType")
    def reset_grantee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGranteeType", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeInput")
    def grantee_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeTypeInput")
    def grantee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "access"))

    @access.setter
    def access(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsOutputReference, "access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="grantee")
    def grantee(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantee"))

    @grantee.setter
    def grantee(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsOutputReference, "grantee").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantee", value)

    @builtins.property
    @jsii.member(jsii_name="granteeType")
    def grantee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "granteeType"))

    @grantee_type.setter
    def grantee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsOutputReference, "grantee_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "granteeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPipelineContentConfigPermissions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineContentConfigPermissionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineNotifications",
    jsii_struct_bases=[],
    name_mapping={
        "completed": "completed",
        "error": "error",
        "progressing": "progressing",
        "warning": "warning",
    },
)
class ElastictranscoderPipelineNotifications:
    def __init__(
        self,
        *,
        completed: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        progressing: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param completed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.
        :param error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.
        :param progressing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.
        :param warning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineNotifications.__init__)
            check_type(argname="argument completed", value=completed, expected_type=type_hints["completed"])
            check_type(argname="argument error", value=error, expected_type=type_hints["error"])
            check_type(argname="argument progressing", value=progressing, expected_type=type_hints["progressing"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
        self._values: typing.Dict[str, typing.Any] = {}
        if completed is not None:
            self._values["completed"] = completed
        if error is not None:
            self._values["error"] = error
        if progressing is not None:
            self._values["progressing"] = progressing
        if warning is not None:
            self._values["warning"] = warning

    @builtins.property
    def completed(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#completed ElastictranscoderPipeline#completed}.'''
        result = self._values.get("completed")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#error ElastictranscoderPipeline#error}.'''
        result = self._values.get("error")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def progressing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#progressing ElastictranscoderPipeline#progressing}.'''
        result = self._values.get("progressing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#warning ElastictranscoderPipeline#warning}.'''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineNotifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineNotificationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineNotificationsOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineNotificationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompleted")
    def reset_completed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompleted", []))

    @jsii.member(jsii_name="resetError")
    def reset_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetError", []))

    @jsii.member(jsii_name="resetProgressing")
    def reset_progressing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProgressing", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @builtins.property
    @jsii.member(jsii_name="completedInput")
    def completed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "completedInput"))

    @builtins.property
    @jsii.member(jsii_name="errorInput")
    def error_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorInput"))

    @builtins.property
    @jsii.member(jsii_name="progressingInput")
    def progressing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "progressingInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="completed")
    def completed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "completed"))

    @completed.setter
    def completed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineNotificationsOutputReference, "completed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "completed", value)

    @builtins.property
    @jsii.member(jsii_name="error")
    def error(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "error"))

    @error.setter
    def error(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineNotificationsOutputReference, "error").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "error", value)

    @builtins.property
    @jsii.member(jsii_name="progressing")
    def progressing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "progressing"))

    @progressing.setter
    def progressing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineNotificationsOutputReference, "progressing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "progressing", value)

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warning"))

    @warning.setter
    def warning(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineNotificationsOutputReference, "warning").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warning", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPipelineNotifications]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineNotifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineNotifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineNotificationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineThumbnailConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "storage_class": "storageClass"},
)
class ElastictranscoderPipelineThumbnailConfig:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfig.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#bucket ElastictranscoderPipeline#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#storage_class ElastictranscoderPipeline#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineThumbnailConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineThumbnailConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineThumbnailConfigOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigOutputReference, "storage_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastictranscoderPipelineThumbnailConfig]:
        return typing.cast(typing.Optional[ElastictranscoderPipelineThumbnailConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPipelineThumbnailConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineThumbnailConfigPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "grantee": "grantee",
        "grantee_type": "granteeType",
    },
)
class ElastictranscoderPipelineThumbnailConfigPermissions:
    def __init__(
        self,
        *,
        access: typing.Optional[typing.Sequence[builtins.str]] = None,
        grantee: typing.Optional[builtins.str] = None,
        grantee_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.
        :param grantee: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.
        :param grantee_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfigPermissions.__init__)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument grantee_type", value=grantee_type, expected_type=type_hints["grantee_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access is not None:
            self._values["access"] = access
        if grantee is not None:
            self._values["grantee"] = grantee
        if grantee_type is not None:
            self._values["grantee_type"] = grantee_type

    @builtins.property
    def access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#access ElastictranscoderPipeline#access}.'''
        result = self._values.get("access")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grantee(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee ElastictranscoderPipeline#grantee}.'''
        result = self._values.get("grantee")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grantee_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline#grantee_type ElastictranscoderPipeline#grantee_type}.'''
        result = self._values.get("grantee_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPipelineThumbnailConfigPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPipelineThumbnailConfigPermissionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineThumbnailConfigPermissionsList",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfigPermissionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfigPermissionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPipelineThumbnailConfigPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetGrantee")
    def reset_grantee(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantee", []))

    @jsii.member(jsii_name="resetGranteeType")
    def reset_grantee_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGranteeType", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeInput")
    def grantee_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeInput"))

    @builtins.property
    @jsii.member(jsii_name="granteeTypeInput")
    def grantee_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "granteeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "access"))

    @access.setter
    def access(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference, "access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="grantee")
    def grantee(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantee"))

    @grantee.setter
    def grantee(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference, "grantee").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantee", value)

    @builtins.property
    @jsii.member(jsii_name="granteeType")
    def grantee_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "granteeType"))

    @grantee_type.setter
    def grantee_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference, "grantee_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "granteeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPipelineThumbnailConfigPermissions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPreset(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPreset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container: builtins.str,
        audio: typing.Optional[typing.Union["ElastictranscoderPresetAudio", typing.Dict[str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union["ElastictranscoderPresetAudioCodecOptions", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPreset.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastictranscoderPresetConfig(
            container=container,
            audio=audio,
            audio_codec_options=audio_codec_options,
            description=description,
            id=id,
            name=name,
            thumbnails=thumbnails,
            type=type,
            video=video,
            video_codec_options=video_codec_options,
            video_watermarks=video_watermarks,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAudio")
    def put_audio(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        value = ElastictranscoderPresetAudio(
            audio_packing_mode=audio_packing_mode,
            bit_rate=bit_rate,
            channels=channels,
            codec=codec,
            sample_rate=sample_rate,
        )

        return typing.cast(None, jsii.invoke(self, "putAudio", [value]))

    @jsii.member(jsii_name="putAudioCodecOptions")
    def put_audio_codec_options(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        value = ElastictranscoderPresetAudioCodecOptions(
            bit_depth=bit_depth, bit_order=bit_order, profile=profile, signed=signed
        )

        return typing.cast(None, jsii.invoke(self, "putAudioCodecOptions", [value]))

    @jsii.member(jsii_name="putThumbnails")
    def put_thumbnails(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetThumbnails(
            aspect_ratio=aspect_ratio,
            format=format,
            interval=interval,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnails", [value]))

    @jsii.member(jsii_name="putVideo")
    def put_video(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetVideo(
            aspect_ratio=aspect_ratio,
            bit_rate=bit_rate,
            codec=codec,
            display_aspect_ratio=display_aspect_ratio,
            fixed_gop=fixed_gop,
            frame_rate=frame_rate,
            keyframes_max_dist=keyframes_max_dist,
            max_frame_rate=max_frame_rate,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putVideo", [value]))

    @jsii.member(jsii_name="putVideoWatermarks")
    def put_video_watermarks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPreset.put_video_watermarks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVideoWatermarks", [value]))

    @jsii.member(jsii_name="resetAudio")
    def reset_audio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudio", []))

    @jsii.member(jsii_name="resetAudioCodecOptions")
    def reset_audio_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioCodecOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetThumbnails")
    def reset_thumbnails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnails", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVideo")
    def reset_video(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideo", []))

    @jsii.member(jsii_name="resetVideoCodecOptions")
    def reset_video_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoCodecOptions", []))

    @jsii.member(jsii_name="resetVideoWatermarks")
    def reset_video_watermarks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoWatermarks", []))

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
    @jsii.member(jsii_name="audio")
    def audio(self) -> "ElastictranscoderPresetAudioOutputReference":
        return typing.cast("ElastictranscoderPresetAudioOutputReference", jsii.get(self, "audio"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptions")
    def audio_codec_options(
        self,
    ) -> "ElastictranscoderPresetAudioCodecOptionsOutputReference":
        return typing.cast("ElastictranscoderPresetAudioCodecOptionsOutputReference", jsii.get(self, "audioCodecOptions"))

    @builtins.property
    @jsii.member(jsii_name="thumbnails")
    def thumbnails(self) -> "ElastictranscoderPresetThumbnailsOutputReference":
        return typing.cast("ElastictranscoderPresetThumbnailsOutputReference", jsii.get(self, "thumbnails"))

    @builtins.property
    @jsii.member(jsii_name="video")
    def video(self) -> "ElastictranscoderPresetVideoOutputReference":
        return typing.cast("ElastictranscoderPresetVideoOutputReference", jsii.get(self, "video"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarks")
    def video_watermarks(self) -> "ElastictranscoderPresetVideoWatermarksList":
        return typing.cast("ElastictranscoderPresetVideoWatermarksList", jsii.get(self, "videoWatermarks"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptionsInput")
    def audio_codec_options_input(
        self,
    ) -> typing.Optional["ElastictranscoderPresetAudioCodecOptions"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudioCodecOptions"], jsii.get(self, "audioCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="audioInput")
    def audio_input(self) -> typing.Optional["ElastictranscoderPresetAudio"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudio"], jsii.get(self, "audioInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

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
    @jsii.member(jsii_name="thumbnailsInput")
    def thumbnails_input(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], jsii.get(self, "thumbnailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptionsInput")
    def video_codec_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "videoCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="videoInput")
    def video_input(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], jsii.get(self, "videoInput"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarksInput")
    def video_watermarks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], jsii.get(self, "videoWatermarksInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptions")
    def video_codec_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "videoCodecOptions"))

    @video_codec_options.setter
    def video_codec_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPreset, "video_codec_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoCodecOptions", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetAudio",
    jsii_struct_bases=[],
    name_mapping={
        "audio_packing_mode": "audioPackingMode",
        "bit_rate": "bitRate",
        "channels": "channels",
        "codec": "codec",
        "sample_rate": "sampleRate",
    },
)
class ElastictranscoderPresetAudio:
    def __init__(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetAudio.__init__)
            check_type(argname="argument audio_packing_mode", value=audio_packing_mode, expected_type=type_hints["audio_packing_mode"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument channels", value=channels, expected_type=type_hints["channels"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument sample_rate", value=sample_rate, expected_type=type_hints["sample_rate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audio_packing_mode is not None:
            self._values["audio_packing_mode"] = audio_packing_mode
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if channels is not None:
            self._values["channels"] = channels
        if codec is not None:
            self._values["codec"] = codec
        if sample_rate is not None:
            self._values["sample_rate"] = sample_rate

    @builtins.property
    def audio_packing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.'''
        result = self._values.get("audio_packing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channels(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.'''
        result = self._values.get("channels")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.'''
        result = self._values.get("sample_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetAudioCodecOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bit_depth": "bitDepth",
        "bit_order": "bitOrder",
        "profile": "profile",
        "signed": "signed",
    },
)
class ElastictranscoderPresetAudioCodecOptions:
    def __init__(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetAudioCodecOptions.__init__)
            check_type(argname="argument bit_depth", value=bit_depth, expected_type=type_hints["bit_depth"])
            check_type(argname="argument bit_order", value=bit_order, expected_type=type_hints["bit_order"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument signed", value=signed, expected_type=type_hints["signed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bit_depth is not None:
            self._values["bit_depth"] = bit_depth
        if bit_order is not None:
            self._values["bit_order"] = bit_order
        if profile is not None:
            self._values["profile"] = profile
        if signed is not None:
            self._values["signed"] = signed

    @builtins.property
    def bit_depth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.'''
        result = self._values.get("bit_depth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.'''
        result = self._values.get("bit_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signed(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.'''
        result = self._values.get("signed")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudioCodecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetAudioCodecOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetAudioCodecOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetAudioCodecOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBitDepth")
    def reset_bit_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitDepth", []))

    @jsii.member(jsii_name="resetBitOrder")
    def reset_bit_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitOrder", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetSigned")
    def reset_signed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigned", []))

    @builtins.property
    @jsii.member(jsii_name="bitDepthInput")
    def bit_depth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="bitOrderInput")
    def bit_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="signedInput")
    def signed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signedInput"))

    @builtins.property
    @jsii.member(jsii_name="bitDepth")
    def bit_depth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitDepth"))

    @bit_depth.setter
    def bit_depth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioCodecOptionsOutputReference, "bit_depth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitDepth", value)

    @builtins.property
    @jsii.member(jsii_name="bitOrder")
    def bit_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitOrder"))

    @bit_order.setter
    def bit_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioCodecOptionsOutputReference, "bit_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitOrder", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioCodecOptionsOutputReference, "profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="signed")
    def signed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signed"))

    @signed.setter
    def signed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioCodecOptionsOutputReference, "signed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudioCodecOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioCodecOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetAudioOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetAudioOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetAudioOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudioPackingMode")
    def reset_audio_packing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioPackingMode", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetChannels")
    def reset_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannels", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetSampleRate")
    def reset_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleRate", []))

    @builtins.property
    @jsii.member(jsii_name="audioPackingModeInput")
    def audio_packing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioPackingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="channelsInput")
    def channels_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelsInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleRateInput")
    def sample_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="audioPackingMode")
    def audio_packing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioPackingMode"))

    @audio_packing_mode.setter
    def audio_packing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "audio_packing_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioPackingMode", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "bit_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="channels")
    def channels(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channels"))

    @channels.setter
    def channels(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "channels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channels", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "codec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleRate"))

    @sample_rate.setter
    def sample_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "sample_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetAudioOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "audio": "audio",
        "audio_codec_options": "audioCodecOptions",
        "description": "description",
        "id": "id",
        "name": "name",
        "thumbnails": "thumbnails",
        "type": "type",
        "video": "video",
        "video_codec_options": "videoCodecOptions",
        "video_watermarks": "videoWatermarks",
    },
)
class ElastictranscoderPresetConfig(cdktf.TerraformMetaArguments):
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
        container: builtins.str,
        audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''AWS Elastic Transcoder.

        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(audio, dict):
            audio = ElastictranscoderPresetAudio(**audio)
        if isinstance(audio_codec_options, dict):
            audio_codec_options = ElastictranscoderPresetAudioCodecOptions(**audio_codec_options)
        if isinstance(thumbnails, dict):
            thumbnails = ElastictranscoderPresetThumbnails(**thumbnails)
        if isinstance(video, dict):
            video = ElastictranscoderPresetVideo(**video)
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument audio", value=audio, expected_type=type_hints["audio"])
            check_type(argname="argument audio_codec_options", value=audio_codec_options, expected_type=type_hints["audio_codec_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbnails", value=thumbnails, expected_type=type_hints["thumbnails"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument video", value=video, expected_type=type_hints["video"])
            check_type(argname="argument video_codec_options", value=video_codec_options, expected_type=type_hints["video_codec_options"])
            check_type(argname="argument video_watermarks", value=video_watermarks, expected_type=type_hints["video_watermarks"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
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
        if audio is not None:
            self._values["audio"] = audio
        if audio_codec_options is not None:
            self._values["audio_codec_options"] = audio_codec_options
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if thumbnails is not None:
            self._values["thumbnails"] = thumbnails
        if type is not None:
            self._values["type"] = type
        if video is not None:
            self._values["video"] = video
        if video_codec_options is not None:
            self._values["video_codec_options"] = video_codec_options
        if video_watermarks is not None:
            self._values["video_watermarks"] = video_watermarks

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
    def container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.'''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audio(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        '''audio block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        '''
        result = self._values.get("audio")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], result)

    @builtins.property
    def audio_codec_options(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        '''audio_codec_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        '''
        result = self._values.get("audio_codec_options")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbnails(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        '''thumbnails block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        '''
        result = self._values.get("thumbnails")
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        '''video block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        '''
        result = self._values.get("video")
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], result)

    @builtins.property
    def video_codec_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.'''
        result = self._values.get("video_codec_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def video_watermarks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        '''video_watermarks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        result = self._values.get("video_watermarks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetThumbnails",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "format": "format",
        "interval": "interval",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetThumbnails:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetThumbnails.__init__)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if format is not None:
            self._values["format"] = format
        if interval is not None:
            self._values["interval"] = interval
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetThumbnails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetThumbnailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetThumbnailsOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetThumbnailsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "aspect_ratio").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "max_height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "max_width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "padding_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "resolution").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "sizing_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetThumbnails]:
        return typing.cast(typing.Optional[ElastictranscoderPresetThumbnails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetThumbnails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetThumbnailsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetVideo",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "bit_rate": "bitRate",
        "codec": "codec",
        "display_aspect_ratio": "displayAspectRatio",
        "fixed_gop": "fixedGop",
        "frame_rate": "frameRate",
        "keyframes_max_dist": "keyframesMaxDist",
        "max_frame_rate": "maxFrameRate",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetVideo:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideo.__init__)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument display_aspect_ratio", value=display_aspect_ratio, expected_type=type_hints["display_aspect_ratio"])
            check_type(argname="argument fixed_gop", value=fixed_gop, expected_type=type_hints["fixed_gop"])
            check_type(argname="argument frame_rate", value=frame_rate, expected_type=type_hints["frame_rate"])
            check_type(argname="argument keyframes_max_dist", value=keyframes_max_dist, expected_type=type_hints["keyframes_max_dist"])
            check_type(argname="argument max_frame_rate", value=max_frame_rate, expected_type=type_hints["max_frame_rate"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if codec is not None:
            self._values["codec"] = codec
        if display_aspect_ratio is not None:
            self._values["display_aspect_ratio"] = display_aspect_ratio
        if fixed_gop is not None:
            self._values["fixed_gop"] = fixed_gop
        if frame_rate is not None:
            self._values["frame_rate"] = frame_rate
        if keyframes_max_dist is not None:
            self._values["keyframes_max_dist"] = keyframes_max_dist
        if max_frame_rate is not None:
            self._values["max_frame_rate"] = max_frame_rate
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.'''
        result = self._values.get("display_aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fixed_gop(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.'''
        result = self._values.get("fixed_gop")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.'''
        result = self._values.get("frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyframes_max_dist(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.'''
        result = self._values.get("keyframes_max_dist")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.'''
        result = self._values.get("max_frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetVideoOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetDisplayAspectRatio")
    def reset_display_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayAspectRatio", []))

    @jsii.member(jsii_name="resetFixedGop")
    def reset_fixed_gop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedGop", []))

    @jsii.member(jsii_name="resetFrameRate")
    def reset_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrameRate", []))

    @jsii.member(jsii_name="resetKeyframesMaxDist")
    def reset_keyframes_max_dist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyframesMaxDist", []))

    @jsii.member(jsii_name="resetMaxFrameRate")
    def reset_max_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFrameRate", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatioInput")
    def display_aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayAspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedGopInput")
    def fixed_gop_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fixedGopInput"))

    @builtins.property
    @jsii.member(jsii_name="frameRateInput")
    def frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDistInput")
    def keyframes_max_dist_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyframesMaxDistInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFrameRateInput")
    def max_frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxFrameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "aspect_ratio").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "bit_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "codec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatio")
    def display_aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayAspectRatio"))

    @display_aspect_ratio.setter
    def display_aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "display_aspect_ratio").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayAspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="fixedGop")
    def fixed_gop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fixedGop"))

    @fixed_gop.setter
    def fixed_gop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "fixed_gop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixedGop", value)

    @builtins.property
    @jsii.member(jsii_name="frameRate")
    def frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frameRate"))

    @frame_rate.setter
    def frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "frame_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameRate", value)

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDist")
    def keyframes_max_dist(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyframesMaxDist"))

    @keyframes_max_dist.setter
    def keyframes_max_dist(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "keyframes_max_dist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyframesMaxDist", value)

    @builtins.property
    @jsii.member(jsii_name="maxFrameRate")
    def max_frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxFrameRate"))

    @max_frame_rate.setter
    def max_frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "max_frame_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFrameRate", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "max_height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "max_width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "padding_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "resolution").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "sizing_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetVideo]:
        return typing.cast(typing.Optional[ElastictranscoderPresetVideo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetVideo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetVideoWatermarks",
    jsii_struct_bases=[],
    name_mapping={
        "horizontal_align": "horizontalAlign",
        "horizontal_offset": "horizontalOffset",
        "id": "id",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "opacity": "opacity",
        "sizing_policy": "sizingPolicy",
        "target": "target",
        "vertical_align": "verticalAlign",
        "vertical_offset": "verticalOffset",
    },
)
class ElastictranscoderPresetVideoWatermarks:
    def __init__(
        self,
        *,
        horizontal_align: typing.Optional[builtins.str] = None,
        horizontal_offset: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        opacity: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        vertical_align: typing.Optional[builtins.str] = None,
        vertical_offset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param horizontal_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.
        :param horizontal_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param opacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.
        :param vertical_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.
        :param vertical_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideoWatermarks.__init__)
            check_type(argname="argument horizontal_align", value=horizontal_align, expected_type=type_hints["horizontal_align"])
            check_type(argname="argument horizontal_offset", value=horizontal_offset, expected_type=type_hints["horizontal_offset"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument opacity", value=opacity, expected_type=type_hints["opacity"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument vertical_align", value=vertical_align, expected_type=type_hints["vertical_align"])
            check_type(argname="argument vertical_offset", value=vertical_offset, expected_type=type_hints["vertical_offset"])
        self._values: typing.Dict[str, typing.Any] = {}
        if horizontal_align is not None:
            self._values["horizontal_align"] = horizontal_align
        if horizontal_offset is not None:
            self._values["horizontal_offset"] = horizontal_offset
        if id is not None:
            self._values["id"] = id
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if opacity is not None:
            self._values["opacity"] = opacity
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy
        if target is not None:
            self._values["target"] = target
        if vertical_align is not None:
            self._values["vertical_align"] = vertical_align
        if vertical_offset is not None:
            self._values["vertical_offset"] = vertical_offset

    @builtins.property
    def horizontal_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.'''
        result = self._values.get("horizontal_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def horizontal_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.'''
        result = self._values.get("horizontal_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.'''
        result = self._values.get("opacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.'''
        result = self._values.get("vertical_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.'''
        result = self._values.get("vertical_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideoWatermarks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoWatermarksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetVideoWatermarksList",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideoWatermarksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPresetVideoWatermarksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideoWatermarksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPresetVideoWatermarksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetVideoWatermarksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoder.ElastictranscoderPresetVideoWatermarksOutputReference",
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
            type_hints = typing.get_type_hints(ElastictranscoderPresetVideoWatermarksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHorizontalAlign")
    def reset_horizontal_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalAlign", []))

    @jsii.member(jsii_name="resetHorizontalOffset")
    def reset_horizontal_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalOffset", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetOpacity")
    def reset_opacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpacity", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetVerticalAlign")
    def reset_vertical_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalAlign", []))

    @jsii.member(jsii_name="resetVerticalOffset")
    def reset_vertical_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalOffset", []))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlignInput")
    def horizontal_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalOffsetInput")
    def horizontal_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="opacityInput")
    def opacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opacityInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalAlignInput")
    def vertical_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalOffsetInput")
    def vertical_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlign")
    def horizontal_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalAlign"))

    @horizontal_align.setter
    def horizontal_align(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "horizontal_align").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="horizontalOffset")
    def horizontal_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalOffset"))

    @horizontal_offset.setter
    def horizontal_offset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "horizontal_offset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "max_height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "max_width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="opacity")
    def opacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opacity"))

    @opacity.setter
    def opacity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "opacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opacity", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "sizing_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="verticalAlign")
    def vertical_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalAlign"))

    @vertical_align.setter
    def vertical_align(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "vertical_align").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="verticalOffset")
    def vertical_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalOffset"))

    @vertical_offset.setter
    def vertical_offset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "vertical_offset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ElastictranscoderPresetVideoWatermarksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastictranscoderPipeline",
    "ElastictranscoderPipelineConfig",
    "ElastictranscoderPipelineContentConfig",
    "ElastictranscoderPipelineContentConfigOutputReference",
    "ElastictranscoderPipelineContentConfigPermissions",
    "ElastictranscoderPipelineContentConfigPermissionsList",
    "ElastictranscoderPipelineContentConfigPermissionsOutputReference",
    "ElastictranscoderPipelineNotifications",
    "ElastictranscoderPipelineNotificationsOutputReference",
    "ElastictranscoderPipelineThumbnailConfig",
    "ElastictranscoderPipelineThumbnailConfigOutputReference",
    "ElastictranscoderPipelineThumbnailConfigPermissions",
    "ElastictranscoderPipelineThumbnailConfigPermissionsList",
    "ElastictranscoderPipelineThumbnailConfigPermissionsOutputReference",
    "ElastictranscoderPreset",
    "ElastictranscoderPresetAudio",
    "ElastictranscoderPresetAudioCodecOptions",
    "ElastictranscoderPresetAudioCodecOptionsOutputReference",
    "ElastictranscoderPresetAudioOutputReference",
    "ElastictranscoderPresetConfig",
    "ElastictranscoderPresetThumbnails",
    "ElastictranscoderPresetThumbnailsOutputReference",
    "ElastictranscoderPresetVideo",
    "ElastictranscoderPresetVideoOutputReference",
    "ElastictranscoderPresetVideoWatermarks",
    "ElastictranscoderPresetVideoWatermarksList",
    "ElastictranscoderPresetVideoWatermarksOutputReference",
]

publication.publish()
