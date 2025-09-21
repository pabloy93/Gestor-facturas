# Alcance del Proyecto

## Objetivo
Crear una plataforma que permita:
- Guardar clientes (personas físicas y morales).
- Recordatorioa personalizados, flujo de informacion, constancia mensual, opinion de cumplimiento semanal, Capturar informacion sobre sus declaraciones, si estan presentadas y si estan pagadas
- Subir y almacenar facturas XML (CFDI).
- Extraer y organizar la información clave de cada XML (UUID, RFC, monto, fecha).
- Relacionar facturas con clientes automáticamente.
- Calcular saldos acumulados por mes.
- Registrar pagos y ver historial por factura/cliente.
- Generar reportes y exportar datos.
- Generar, riesgos, y calcular parametros de alerta, checar a cuales les falta REP

## Usuarios del sistema
- **Administrador**: controla todo, maneja clientes, facturas, pagos y reportes.
- **Contador**: gestiona clientes y facturas, registra pagos.
- **Consulta**: solo puede ver información Y revisar saldos mensuales mediante un chatboot de whatsapp.

## Entidades principales
- **Cliente**: RFC, razón social, datos de contacto, regimen fiscal, honorarios, si tiene empleados, espacio para notas.
- **Factura (XML)**: UUID, RFC emisor/receptor, fecha, subtotal, total, IVA, método de pago, estado, folio, si cuenta con REP(cuando son PDD).
- **Pago**: monto, fecha, método, Meses que pago.
- **Usuario**: login, contraseña, rol.
- **Consulta**: Recibir reportes en chatboot de whatsapp

## Casos de uso clave
1. Crear/editar/borrar clientes.
2. Subir un XML → guardar archivo → parsear → registrar datos en DB.
3. Relacionar factura con cliente por RFC.
4. Registrar un pago y descontar saldo pendiente.
5. Consultar facturación mensual por cliente.
6. Generar reportes (pantalla y exportación a Excel/CSV).
7. Generar Reportes de Cuanto se Cobra y Cuando Paga.
