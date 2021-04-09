* Terraform promary function is to create, modify, and destroy infrastructure resources to match
the desired state described in a Terraform configuration.
* specify provider version:  >=x  <=x   ~>x.x ( any version in the range)    >=x,<=x   ( between) = ( specific version)
* Version chages not into effect unless u delete .terraform.lock.hd file. or terraform init --upgrade. lock file for newer versions 
* Terraform automatically converts number and bool values to strings when needed.
* Consul remote stettefile locking - out of the box
* Sentinel - A proactive approach focuses on eliminating problems before they have a chance to appear and a reactive approach is based on responding to events after they have happened
* Terraform state file stores which type of dependency information? implicit and explicit
* if you see ~ in terraform apply. it' sin place upgrade

**certain changes leads to destroy the insyance and recreate. ex. changing from t2 micro to t3.medium ( ebs optimized)

<details open>
<summary>Providors:</summary>

Terraform supports providers. 
```
provider "aws" {
  region     = "us-east-1"
  access_key = "xxx"
  secret_key = "xxx"
}
```

From 0.13 onwards Terraform requires explicit source information for any provider that are not hashicorp maintained, using a new syntax in the *required_providers* block inside.the terraform configuration block.

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
```
</details>  



<details open>
<summary>Resources:</summary>

Resources expect certain types of arguments. some requires and some not.
Resources are the reference to the individual services which the provider has to offer.

```
resource "aws_instance" "web" {
  ami           = "ami-038f1ca1bd58a5790"
  //instance_type =  var.instance-types-map["us-east-1"]
  instance_type =  var.instance-types-list[0]

  tags = {
    Name = "HelloWorld"
  }
}
```
</details> 


<details open>
<summary>Funcrions:</summary>


* String
* Numeric
* Encoading
* Date and Time 
* Hash and Crypto 
* IP Network
* Typr conversion
</details>


<details open>
<summary>Terraform Commands:</summary>

* Terraform does not case any other changes that' snot mentioned on code. i.e. desired state
* terraform destroy -auto-approve
* terrraform destroy -target=<resource type + resource name>
* terraform destroy -target <resource type>.<local resource name><[if any]>
* terraform refresh   ( fetch current state of resource and also update the state file )
* terraform plan ( refresh statefile as well )
* terraform init -upgrade // upgrade plugins
* terraform console to validate expressions.
</details>


<details open>
<summary>state management:</summary>

* terraform state <command>
   * list       terraform state list   ( list resources with in terraform state)
   * mv         terraform state mv <options> <source> <destination>  ( to rename resources etc.)
   * pull    manually download and output the state from remote state
   * push    manually upload a local state to remote ste
   * rm      remove items from terraform state. no longer managed by tf. 
   * show  <resource name>  show the attributes of a single resource in tf state
</details>


<details open>
<summary>Attributes and output values:</summary>

Referencing of attribute to another resource. 

```
resource "aws_eip" "lb" {
     vpc = true
}

resource "aws_eip_association" "eip_assoc" {
    instance_id = aws_instance.myec2.if
    allocation_if = aws_eip.lb.id
}
```
</details>


<details open>
<summary>Terraform Variables:</summary>
- envirnment variables.
- Command line flags  -var="xxx=yyy"
- from a file - i fnot .tfvars then  -var-file=custom.vars
- variable defaults
</details>


<details open>
<summary>Data Types:</summary>
- String
- List
- Map
- Number

```
variable "list" {
    type = list
    default = ["m5.large", "m5.xlarge"]
}

variable "maptype" {
    type = map
    default {
        us-east-1 = "t2.micro"
        us-west-2 = "t2.nano"
    }
}

resource "aws_instance' "myec2" {
    
    instance_type =  var.maptype["us-east-1"]
    instance_type =  var.list["0]
}
```
</details>


<details open>
<summary>count and count index:</summary>

it's lets you scale the resource by incrementing.

```
resource "aws_instance' "myec2" {
    count = 5
    instance_type =  xxxxx
}

variable "listofiamusers' {
    type = list
    default = ["tom", "pom", "dom"]
}

resource 'aws_iam_user" "lb" {
    count = 3
    name = var.listofiamusers[count.index]
}
```
</details>



<details open>
<summary>conditional expression:</summary>

condition ? true_val : false_val

count = var.test == false ? 1 : 0
</details>


<details open>
<summary>Local Values:</summary>

A local value assigns a name to an expression, allowing it to be used multiple times within a module withour repeating it.

we can use where singl evalue used in multiple places.

```
locals {
    common_tags = {
        owner = "tom"
        service = web
    }
}

resource 'aws_iam_user" "lb" {
    count = 3
    name = var.listofiamusers[count.index]
    tags = local.common_tags
}
```

Local Values can be used for multiple diffrent use-cases like having a conditional expressions.

```
locals {
    name_prefix = "$var.name != "" ? var.name : var.default}"
}

locals {
    instance_ids = contact(aws_instance.blue.*.id,aws_instance.green.*.id)
}
```
</details>



<details open>
<summary>Terraform Functions:</summary>

The terraform launguage includes a number of built-in functions that you can use to transform and combine values. general syntax is functionname(x.x.x)

terraform does not support user defined functions.

max(5,12,9)

split, join, lower, replace etc.

lookup(map, key, default)

```
lookup({a="b", c="d"}, "a", "haha")
b
lookup({a="b", c="d"}, "c", "haha")
haha

variable "ami'{
    type = map
    default = {
         "us-east-1" = "ami-xx"
         "us-west-1" = "ami-uyyy"
    }
}

ami = lookup(var.ami, var.region)
```

```

element(list. index)

list = ["a","b","c"]
Name = element(list,count.index)

```

reads content and return the string 

file(path)

```
public_key = file("${path.moduke}/id_rsa.pub)
```

```
locals{
    time = formatdate("DD MM YYYY hh:mm ZZZ", timestamp())
}

output "timestamp" {
    value = local.time
}
```
</details>



<details open>
<summary>Data Sources:</summary>

Defined under Dta block.

Reads from specific data source (aws_ami) and exports results under "app_ami"

```
data "aws_ami" "app_ami" {
    most_recent = true
    owners = ["amazon"]

    filter {
        name = "name"
        values = ["amzn2-ami-hvm*"]
    }
}

resource "aws_instance" "instance-1"{
    ami = data.aws_ami.app_ami.id
    instance_type = "t2.micro"
}
```
</details>


<details open>
<summary>Debugging in Terraform:</summary>

- TF_LOG - TRACE DEBUG INFO WARN ERROR
- TF_LOG_PATH=
</details>


<details open>
<summary>Terraform Format:</summary>

- terraform fmt
</details>


<details open>
<summary>validating terraform configuration files:</summary>

- Terraform validate promarly checks whether a configuration is syntactically valid.
- it can check various things like unsupported arguments, undeclared variables and otherrs.
- terraform validate
- terraform plan also does behind the scenes.
</details>


<details open>
<summary>Dynamic Blocks:</summary>

In many cases, there are repeatable nested blocks that needs to be defined.

This can lead to a long code it can be defivult to manage in a longer time.

```
ingress {
   from_port = 8300
   to_port   = 8300
   protocol = "tcp"
   cidr_block = ["0.0.0.0/0"]
}

variable "sg_ports" {
  type = list(number)
  description = "list o fports for ingress"
  default = [8080, 9090, 9091, 80, 443]
}

resource "aws_security_group" "dynamicsg" {
  name = "dymamic-sg"
  description = "ingress for web vm"

  dynamic "ingress" {
     for_each = var.sg_ports
     //iterator = port
     content {
           //from_port = port.value
           //to_port = port.value
           from_port = ingress.value
           to_port = ingress.value
           protocol = "tcp"
           cidr_blocks = ["0.0.0.0/0"]
     }
  }
}
```
</details>


<details open>
<summary>Tainting Resources:</summary>

Assume, you created a respurce but some other user made manual changes.

Two ways to deal with it:
- Import the changes to Terraform.
- Delete & recreate the resource.

The terraform taint ommand manually marks a terraform-managed resource as tainted, forcing it to be destroyed and recreated on the next apply.

terraform taint xxx
</details>


<details open>
<summary>Splat Expressions:</summary>

Splat expressions allows to get list of  all the attributes

```
resource "aws_iam_user" "lb" {
    name = "iamuser.$cout.index}"
    counnt = 3
    path ="/system"
}

output "arns" {
    value = aws_iam_user.lb[*].arn
}
```
</details>


<details open>
<summary>terraform graph:</summary>

- terraform graph > xxx.dot 
- command is used to generate a visual representation of either a configuration or execution plan
- theoutput is DOR format and can be convertable to an image.
- graphviz visualization package.

#saving terraform plan to file
  - terraform plan -out=path  - generate binary file
  - terraform show <file>


#terraform output command is used to extract the value of an utput variable from the state file.
  - terraform output <output variable>

```
#terraform settings
    terraform {
       required_version = "> 0.12.0" // <--
       required_providers {
         aws = {
            source  = "hashicorp/aws"
            version = "~> 3.0"
          }
       }
    }
```
</details>


<details open>
<summary>Dealing with Larger Infrastructure:</summary>


- API call limits for provider ?
- x.tf (ec2, eds, sg)    / ec2.tf  rds.tf sg.tf vpc.tf - seperate folders
- you can pass -refresh=false flag. to terraform plan
- specify target  -target=targetname
</details>


<details open>
<summary>Zip Map:</summary>

```
zipmap([a,b],[c,d])
{
    a=c,
    b=d
}
```
</details>


<details open>
<summary>Terraform Provisioners:</summary>

- remote_exec
- local_exce

```
resource "aws_instance" "apache" {
  ami           = "ami-038f1ca1bd58a5790"
  instance_type  = "t2.micro"
  key_name = "tf-training"
  
  provisioner "remote-exec" {
    // inline for list of commands
     inline = [
          "sudo amazon-linux-extras install -y nginx1.12",
          "sudo systemctl start nginx"
     ]
  } 
  
   provisioner "remote-exec" {
     when = destroy
    // inline for list of commands
     inline = [
          "sudo systemctl stop nginx",
          "for i in {1..20}; do echo hello; sleep 2;done"
     ]

   }  

   connection {
        type = "ssh"
        user = "ec2-user"
        private_key = file("./tf-training.pem")
        host = self.public_ip
   }
  
  provisioner "local-exec" {
      command = "echo ${aws_instance.apache.private_ip} > private_ips.txt"
  }

  provisioner "local-exec" {
      when = destroy
      command = "echo destroyed > private_ips.txt"
  }
  }
  ```

- provisioner Types:
    - Creation-Time provisioner: 
    - Destroy-Time provisioner:  when = "destroy"

- Provisioner Failure behaviour: 
    - on_failure = continue/fail
</details>


<details open>
<summary>user data:</summary>

```
provider "aws" {
	region = "us-east-1"
}

resource "aws_key_pair" "terraform-demo" {
  key_name   = "terraform-demo"
  public_key = "${file("terraform-demo.pub")}"
}

resource "aws_instance" "my-instance" {
	ami = "ami-04169656fea786776"
	instance_type = "t2.nano"
	key_name = "${aws_key_pair.terraform-demo.key_name}"
	user_data = << EOF
		#! /bin/bash
                sudo apt-get update
		sudo apt-get install -y apache2
		sudo systemctl start apache2
		sudo systemctl enable apache2
		echo "<h1>Deployed via Terraform</h1>" | sudo tee /var/www/html/index.html
	EOF
	tags = {
		Name = "Terraform"	
		Batch = "5AM"
	}
}
```

```
provider "aws" {
	region = "us-east-1"
}

resource "aws_key_pair" "terraform-demo" {
  key_name   = "terraform-demo"
  public_key = "${file("terraform-demo.pub")}"
}

resource "aws_instance" "my-instance" {
	ami = "ami-04169656fea786776"
	instance_type = "t2.nano"
	key_name = "${aws_key_pair.terraform-demo.key_name}"
	user_data = "${file("install_apache.sh")}"
	tags = {
		Name = "Terraform"	
		Batch = "5AM"
	}
}
```
</details>


<details open>
<summary>Data source:</summary>

- template_cloudinit_config
- template_file

```
# Render a part using a `template_file`
data "template_file" "script" {
  template = "${file("${path.module}/init.tpl")}"

  vars = {
    consul_address = "${aws_instance.consul.private_ip}"
  }
}

# Render a multi-part cloud-init config making use of the part
# above, and other source files
data "template_cloudinit_config" "config" {
  gzip          = true
  base64_encode = true

  # Main cloud-config configuration file.
  part {
    filename     = "init.cfg"
    content_type = "text/cloud-config"
    content      = "${data.template_file.script.rendered}"
  }

  part {
    content_type = "text/x-shellscript"
    content      = "baz"
  }

  part {
    content_type = "text/x-shellscript"
    content      = "ffbaz"
  }
}

# Start an AWS instance with the cloud-init config as user data
resource "aws_instance" "web" {
  ami              = "ami-d05e75b8"
  instance_type    = "t2.micro"
  user_data_base64 = "${data.template_cloudinit_config.config.rendered}"
}
```


```
data "template_file" "init" {
  template = "${file("${path.module}/init.tpl")}"
  vars = {
    consul_address = "${aws_instance.consul.private_ip}"
  }
}

#!/bin/bash

echo "CONSUL_ADDRESS = ${consul_address}" > /tmp/iplist

user_data = <<-EOT
    echo "CONSUL_ADDRESS = ${aws_instance.consul.private_ip}" > /tmp/iplist
EOT
```
</details>




<details open>
<summary>Terraform workspace:</summary>

- terraform workspace
- terraform workspace show
- terraform workspace new <workspace name>
- terraform workspace select <workspace name>
- terraform maintains tfstate files for each workspace terraform.tfstate.d/<workspace name>
- tfstate file for default workspace is created under main dir.
  
```  
  resource "aws_instance" "my_ec2" {
    ami = "amiid"
    instance_type = lookup(var.instance_type,terraform.workspace)
  }

  varisble "instance_type" {
      type = "map"

      default {
          default = "t2.micro"
          dev = "t1.micro"
          prod = "t2.nano"
      }
  }
```
</details>


<details open>
<summary>Terraform Module Sources:</summary>

Terraform registry contains providor and modules.

  - Local paths  source = "../test"
  - git          source = "git::https://example.com/test.git?ref=v1.2.0"
  - github       source = 
   
```  
module "myfolder' {
    source = 'test/"
}
```
</details>


<details open>
<summary>git ignore:</summary>

  -  .terraform   terraform.tfvars   terraform.tfstate crash.log
</details>


<details open>
<summary>terraform statefile locking:</summary>

- Integrating DynamoDB with S3 for state locking. create Dynamodb Table with LockID

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  backend "s3" {
     bucket = "tf-state-remote-rj"
     key  = "remotedemo.tfstate"
     region = "us-east-1"
     access_key = "xxxx"
     secret_key = "xxxx"
    //dynamodb_table = "tf-state-remote-rj"

  }
}
```
</details>



<details open>
<summary>import:</summary>

- create resources with existing values.
- terraform import aws_instance.myec2 <instance ID>
</details>


<details open>
<summary>alias:</summary>

- alias variable in provider configuration allows to maintain multiple provider configurations

```
   provider "aws" {
     region     = "us-east-1"
     access_key = "xx"
     secret_key = "xxxxxxx"
   }
   provider "aws" {
     alias = "prod"
     region     = "us-east-2"
     access_key = "xx"
     secret_key = "xxxxxxx"
     #profile = "notdefault"
   }

   resource "aws_eip" "xx" {

   }
   resource "aws_eip" "yy" {
     provider = "aws.prod"
   }
```
</details>

<details open>
<summary>handling multiple AWS progile:</summary>

```
  aws s3 ls --profile xxx
  [default]
     access_key=
     sec_access_key=
  [test1]
    access_key=
    sec_access_key=
  
   provider "aws" {
     region     = "us-east-1"
   }
   provider "aws" {
     alias = "prod"
     region     = "us-east-2"
     profile = "notdefault"
   }

   resource "aws_eip" "xx" {

   }
   resource "aws_eip" "yy" {
     provider = "aws.prod"
   }
```
</details>


<details open>
<summary>Terraform assume role with:</summary>

if muyltipl accounts exist.. 
```
  aws sts assume-role  --role-arn  <arn> --role-session-name <session name>
  when terraform needs to assume role.
  provider "aws" {
      region     = "us-east-1"
      assume_role {
         role_arn = ""
         session_name = ""
      }
   }
```
</details>


<details open>
<summary>sensitive parameter:</summary>

- sensitive = true  #in output
- still exist in state file

#cloud
  - organizations - work spaces 
  - Sentinal - Policy as code
</details>


- A variable named instance_type has been undefined within the child module
- variable instance_type {}
- Will the root module be able to set that variable? YES
- Matthew has created a new workspace named "DEV". Do Matthew needs to manually switch to the DEV workspace in order to start using it? FALSE
- TF_VAR_<variable name>=xx


















