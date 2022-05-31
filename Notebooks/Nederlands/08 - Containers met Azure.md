---
created: 2022-05-25T16:17:02 (UTC +02:00)
tags: []
source: chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html
author: tejaswikolli-web
---

#

> ## Excerpt

> Quickly learn to create a private Docker registry in Azure Container Registry with PowerShell

---

## Snelstart: een privécontainerregister maken met Azure PowerShell

- Artikel
- 10/24/2021
- 3 minuten om te lezen

### Is this page helpful?

Feedback will be sent to Microsoft: By pressing the submit button, your feedback will be used to improve Microsoft products and services. [Privacy policy.](https://privacy.microsoft.com/en-us/privacystatement)

Thank you.

### In this article

1. [Prerequisites](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#prerequisites)
2. [Sign in to Azure](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#sign-in-to-azure)
3. [Create resource group](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#create-resource-group)
4. [Create container registry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#create-container-registry)
5. [Log in to registry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#log-in-to-registry)
6. [Push image to registry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#push-image-to-registry)
7. [Run image from registry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#run-image-from-registry)
8. [Clean up resources](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#clean-up-resources)
9. [Next steps](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#next-steps)

Azure Container Registry is een privéregisterservice voor het bouwen, opslaan en beheren van containerinstallatiekopieën en gerelateerde artefacten. In deze quickstart maakt u een Azure-containerregister-exemplaar met Azure PowerShell. Gebruik vervolgens Docker-opdrachten om een containerinstallatiekopie in het register te pushen en trek ten slotte de installatiekopie uit uw register en voer deze uit.

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#prerequisites)Voorwaarden

Notitie

In dit artikel wordt de Azure Az PowerShell-module gebruikt, de aanbevolen PowerShell-module voor interactie met Azure. Zie Azure PowerShell installeren om aan de slag te gaan met de Az [PowerShell-module](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/azure/install-az-ps). Zie [Azure PowerShell migreren van AzureRM naar Az](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/azure/migrate-from-azurerm-to-az) voor meer informatie over het migreren naar de Az PowerShell-module.

Voor deze snelstartgids is een Azure PowerShell-module vereist. Voer uit om uw geïnstalleerde versie te bepalen. Als u Azure [PowerShell-module](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/azure/install-az-ps) moet installeren of upgraden.`Get-Module -ListAvailable Az`

Docker moet ook lokaal zijn geïnstalleerd. Docker biedt pakketten voor [macOS-](https://docs.docker.com/docker-for-mac/), [Windows](https://docs.docker.com/docker-for-windows/)\- en [Linux-systemen](https://docs.docker.com/engine/installation/#supported-platforms).

Omdat de Azure Cloud Shell niet alle vereiste Docker-onderdelen (de daemon) bevat, kunt u de Cloud Shell niet gebruiken voor deze snelstart.`dockerd`

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#sign-in-to-azure)Aanmelden bij Azure

Meld u aan bij uw [Azure-abonnement met de opdracht Connect-AzAccount](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/module/az.accounts/connect-azaccount) en volg de aanwijzingen op het scherm.

```
Connect-AzAccount
```

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#create-resource-group)Resourcegroep maken

Zodra u bent geverifieerd met Azure, maakt u een resourcegroep met [New-AzResourceGroup](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/module/az.resources/new-azresourcegroup). Een resourcegroep is een logische container waarin u uw Azure-resources implementeert en beheert.

```
New-AzResourceGroup -Name myResourceGroup -Location EastUS
```

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#create-container-registry)Containerregister maken

Maak vervolgens een containerregister in uw nieuwe brongroep met de opdracht [New-AzContainerRegistry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/module/az.containerregistry/New-AzContainerRegistry).

De registernaam moet uniek zijn in Azure en 5-50 alfanumerieke tekens bevatten. In het volgende voorbeeld wordt een register met de naam 'myContainerRegistry007' gemaakt. Vervang _myContainerRegistry007_ in de volgende opdracht en voer deze uit om het register te maken:

```
$registry = New-AzContainerRegistry -ResourceGroupName "myResourceGroup" -Name "myContainerRegistry007" -EnableAdminUser -Sku Basic
```

Fooi

In deze quickstart maakt u een _Basisregister_, een kostengeoptimaliseerde optie voor ontwikkelaars die meer te weten komen over Azure Container Registry. Kies andere lagen voor meer opslag en beelddoorvoer en mogelijkheden zoals verbinding via een [privé-eindpunt](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/container-registry-private-link). Zie [Containerregisterservicelagen](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/container-registry-skus) voor meer informatie over beschikbare servicelagen (SKU's).

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#log-in-to-registry)Aanmelden bij het register

Voordat u containerinstallatiekopieën pusht en ophaalt, moet u zich aanmelden bij uw register met de cmdlet [Connect-AzContainerRegistry](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/module/az.containerregistry/connect-azcontainerregistry). In het volgende voorbeeld worden dezelfde referenties gebruikt waarmee u zich hebt aangemeld bij verificatie bij Azure met de cmdlet.`Connect-AzAccount`

Notitie

In het volgende voorbeeld is de waarde van de bronnaam, niet de volledig gekwalificeerde registernaam.`$registry.Name`

```
Connect-AzContainerRegistry -Name $registry.Name
```

De opdracht keert terug zodra deze is voltooid.`Login Succeeded`

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#push-image-to-registry)Afbeelding naar register pushen

Als u een installatiekopie naar een Azure Container-register wilt pushen, moet u eerst een installatiekopie hebben. Als u nog geen lokale containerinstallatiekopieën hebt, voert u de volgende [docker pull-opdracht uit](https://docs.docker.com/engine/reference/commandline/pull/) om een bestaande openbare installatiekopie op te halen. Haal in dit voorbeeld de installatiekopie op uit Microsoft Container Registry.`hello-world`

```
docker pull mcr.microsoft.com/hello-world
```

Voordat u een installatiekopie naar uw register kunt pushen, moet u deze taggen met de volledig gekwalificeerde naam van uw registeraanmeldingsserver. De naam van de aanmeldingsserver heeft de indeling _<registry-name>.azurecr.io_ (moet allemaal kleine letters zijn), bijvoorbeeld _mycontainerregistry.azurecr.io_.

Tag de afbeelding met de [opdracht docker tag](https://docs.docker.com/engine/reference/commandline/tag/). Vervang door de naam van de aanmeldingsserver van uw ACR-instantie.`<login-server>`

```
docker tag mcr.microsoft.com/hello-world <login-server>/hello-world:v1
```

Voorbeeld:

```
docker tag mcr.microsoft.com/hello-world mycontainerregistry.azurecr.io/hello-world:v1
```

Gebruik ten slotte [docker push](https://docs.docker.com/engine/reference/commandline/push/) om de installatiekopie naar de registerinstantie te pushen. Vervang door de naam van de aanmeldingsserver van uw registerinstantie. In dit voorbeeld wordt de **hello-world** repository gemaakt, die de afbeelding bevat.`<login-server>``hello-world:v1`

```
docker push <login-server>/hello-world:v1
```

Nadat u de installatiekopie naar uw containerregister hebt gepusht, verwijdert u de installatiekopie uit uw lokale Docker-omgeving. (Met deze [opdracht docker rmi](https://docs.docker.com/engine/reference/commandline/rmi/) wordt de installatiekopie niet verwijderd uit de **hello-world-opslagplaats in uw Azure-containerregister**.)`hello-world:v1`

```
docker rmi <login-server>/hello-world:v1
```

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#run-image-from-registry)Run image from registry

Now, you can pull and run the container image from your container registry by using [docker run](https://docs.docker.com/engine/reference/commandline/run/):`hello-world:v1`

```
docker run <login-server>/hello-world:v1  
```

Example output:

```
Unable to find image 'mycontainerregistry.azurecr.io/hello-world:v1' locally
v1: Pulling from hello-world
Digest: sha256:662dd8e65ef7ccf13f417962c2f77567d3b132f12c95909de6c85ac3c326a345
Status: Downloaded newer image for mycontainerregistry.azurecr.io/hello-world:v1

Hello from Docker!
This message shows that your installation appears to be working correctly.

[...]
```

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#clean-up-resources)Clean up resources

Once you're done working with the resources you created in this quickstart, use the [Remove-AzResourceGroup](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/en-us/powershell/module/az.resources/remove-azresourcegroup) command to remove the resource group, the container registry, and the container images stored there:

```
Remove-AzResourceGroup -Name myResourceGroup
```

## [](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/_generated_background_page.html#next-steps)Next steps

In this quickstart, you created an Azure Container Registry with Azure PowerShell, pushed a container image, and pulled and ran the image from the registry. Continue to the Azure Container Registry tutorials for a deeper look at ACR.

___

## Recommended content

- [

### Push & pull container image - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli>)

    Push and pull Docker images to your private container registry in Azure using the Docker CLI

- [

### View repositories in portal - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-repositories>)

    Use the Azure portal to view Azure Container Registry repositories, which host Docker container images and other supported artifacts.

- [

### Quickstart - Create registry - Azure CLI - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli>)

    Quickly learn to create a private Docker container registry with the Azure CLI.

- [

### Quickstart - Create registry in portal - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal>)

    Quickly learn to create a private Azure container registry using the Azure portal.

- [

### Tutorial - Build image on code commit - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-tutorial-build-task>)

    In this tutorial, you learn how to configure an Azure Container Registry Task to automatically trigger container image builds in the cloud when you commit source code to a Git repository.

- [

### Registry authentication options - Azure Container Registry

    ](<https://docs.microsoft.com/en-us/azure/container-registry/container-registry-authentication>)

    Authentication options for a private Azure container registry, including signing in with an Azure Active Directory identity, using service principals, and using optional admin credentials.

- [

### Tutorial - Deploy multi-container group - YAML - Azure Container Instances

    ](<https://docs.microsoft.com/en-us/azure/container-instances/container-instances-multi-container-yaml>)

    In this tutorial, you learn how to deploy a container group with multiple containers in Azure Container Instances by using a YAML file with the Azure CLI.

- [

### Tutorial - Prepare container registry to deploy image - Azure Container Instances

    ](<https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-acr>)

    Azure Container Instances tutorial part 2 of 3 - Prepare an Azure container registry and push an image

## Feedback

Submit and view feedback for
