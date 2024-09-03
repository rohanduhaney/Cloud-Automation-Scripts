# Variables
$ResourceGroupName = "myResourceGroup"
$Location = "EastUS"
$VMName = "myVM"
$Image = "UbuntuLTS"
$Size = "Standard_DS1_v2"

# Create Resource Group
New-AzResourceGroup -Name $ResourceGroupName -Location $Location

# Create Virtual Machine
New-AzVM -ResourceGroupName $ResourceGroupName -Name $VMName -Location $Location -ImageName $Image -Size $Size

Write-Output "Virtual Machine $VMName has been created in resource group $ResourceGroupName."
