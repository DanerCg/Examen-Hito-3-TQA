# Escenarios Gherkin (actividad adicional)

Los siguientes escenarios describen el comportamiento de dos funcionalidades de SauceDemo y mantienen coherencia con los casos de prueba diseñados. Gherkin describe escenarios; por sí solo no automatiza las pruebas.

## 1. Funcionalidad: Inicio de sesión

```gherkin
Feature: Inicio de sesión
  Como usuario de SauceDemo
  Quiero iniciar sesión con mis credenciales
  Para acceder al catálogo de productos

  Scenario: Acceso exitoso
    Given que estoy en la página de login
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And hago clic en el botón "Login"
    Then debería ver la página de productos con el título "Products"

  Scenario: Credenciales incorrectas
    Given que estoy en la página de login
    When ingreso el usuario "usuario_invalido" y una contraseña inválida
    And hago clic en el botón "Login"
    Then debería mostrarse un mensaje de error de credenciales
    But no debería acceder a la página de productos

  Scenario: Usuario bloqueado
    Given que estoy en la página de login
    When ingreso el usuario "locked_out_user" y la contraseña "secret_sauce"
    And hago clic en el botón "Login"
    Then debería mostrarse un mensaje indicando que el usuario ha sido bloqueado
```

## 2. Funcionalidad: Carrito y compra

```gherkin
Feature: Carrito y compra
  Como usuario autenticado
  Quiero agregar productos al carrito y realizar el checkout
  Para completar una compra

  Scenario: Agregar un producto al carrito
    Given que inicié sesión como "standard_user"
    And estoy en la página de productos
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el ícono del carrito debería mostrar el contador "1"
    And el botón del producto debería cambiar a "Remove"

  Scenario: Checkout con datos obligatorios vacíos
    Given que inicié sesión como "standard_user"
    And tengo el producto "Sauce Labs Backpack" en el carrito
    And estoy en el formulario de información del checkout
    When dejo los campos vacíos y hago clic en "Continue"
    Then debería mostrarse el mensaje "Error: First Name is required"
    But no debería avanzar al resumen de la compra
```
