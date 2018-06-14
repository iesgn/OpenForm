# OpenForm

## Qué es OpenForm?

Es una aplicación web, desarrollada en Django, que permite crear infraestructura como código. OpenForm está desarrollado para utilizar la herramienta de Hashicorp, *Terraform* y el lenguaje HCL, desarrollado por la misma compañía.

OpenForm es el proyecto integrado para el ciclo formativo de grado superior, que estoy cursando actualmente.

## ¿Porqué Terraform?

En esta decisión influyeron varios factores. El primer factor fue porque cuando empecé este proyecto, iba a entrar en una empresa dónde se utilizaba esta herramienta y quería aprender a utilizarla. El segundo factor fue porque me parecía una herramienta muy interesante, durante el curso para el cual es este proyecto, había podido utilizar la herramienta varias veces, con el proveedor OpenStack, y ya pude ver un poco el potencial de esta herramienta.

Terraform incorpora muchas funcionalidades y una enorme lista de proveedores soportados. Es una de las aplicaciones más utilizadas hoy en día para crear infraestructura como código.

Cuando empecé a utilizar Terraform, tenía la sensación de que la definición de la infraestructura sería muy diferente, dependiendo del proveedor que fuese a utilizar, pero tras varios meses trabajando con esta herramienta, me he dado cuenta que no es tanta la diferencia.

## ¿Porqué HCL?

Esta es una de las cuestiones que más tiempo me ha costado de decidir. Terraform soporta dos lenguajes para la definición de infraestructura, HCL y JSON. En un primer momento me decanté por JSON, ya que es un lenguaje estandarizado y muy conocido. Pero hay un factor que veía necesario en la infraestructura como código y me hizo elegir HCL, *los comentarios*. Voy a dejar un ejemplo de un recurso definido tanto en JSON como en HCL, y veréis como los comentarios son esenciales.

Ejemplo de una instancia de OpenStack en formato JSON:

```json
{
    "resource": {
        "openstack_compute_instance_v2": {
            "orbit": {
                "image_id": "f67e34fb-108d-4418-9a49-4a2dbde5a8f1",
                "security_groups": [
                    "api_network",
                    "tunel_network"
                ],
                "key_pair": "os-admin",
                "flavor_id": "44",
                "name": "orbit"
            }
        }
    }
}
```

Ejemplo de una instancia de OpenStack en formato HCL:

```hcl
# OpenStack compute node
resource "openstack_compute_instance_v2" "orbit" {
  name = "orbit"
  image_id = "f67e34fb-108d-4418-9a49-4a2dbde5a8f1" # Debian 9.2
  flavor_id = "44" # 2GB RAM, 2 CPU cores, 50 GB disk
  key_pair = "os-admin"  # OS Project
  security_groups = ["api_network","tunel_network"]
}
```

Toda la información sobre la aplicación podéis encontrarla en la [wiki del proyecto](https://github.com/sfbenitez/OpenForm/wiki).
