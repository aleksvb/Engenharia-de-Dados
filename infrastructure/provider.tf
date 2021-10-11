provider "aws" {
  region = "us-east-2"
}


#centralizar o status do terraform

terraform{
  backend "s3" {
    bucket = "terraform-state-igti-aleksandro"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}