## 📖 Dicionário de Dados: Hotel Booking Demand

| Coluna | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| `hotel` | Categórico | Tipo de hotel (ex: 'Resort Hotel' ou 'City Hotel'). |
| `is_canceled` | Numérico (Binário) | Indica se a reserva foi cancelada (1) ou não (0). |
| `lead_time` | Numérico | Número de dias entre a data da reserva e a data de chegada. |
| `arrival_date_year` | Numérico | Ano da data de chegada (ex: 2015, 2016, 2017). |
| `arrival_date_month` | Categórico | Mês da data de chegada (ex: 'July', 'August'). |
| `arrival_date_week_number` | Numérico | Número da semana (do ano) da data de chegada. |
| `arrival_date_day_of_month` | Numérico | Dia do mês da data de chegada. |
| `stays_in_weekend_nights` | Numérico | Número de noites de fim de semana (Sábado ou Domingo) da estadia. |
| `stays_in_week_nights` | Numérico | Número de noites de semana (Segunda a Sexta) da estadia. |
| `adults` | Numérico | Número de adultos. |
| `children` | Numérico | Número de crianças. |
| `babies` | Numérico | Número de bebês. |
| `meal` | Categórico | Tipo de refeição reservada (ex: 'BB' - Bed & Breakfast, 'HB' - Half board, 'SC' - Sem refeição). |
| `country` | Categórico | País de origem do hóspede (ex: 'PRT' - Portugal, 'GBR' - Grã-Bretanha). |
| `market_segment` | Categórico | Segmento de mercado da reserva (ex: 'Online TA' - Agente de Viagem Online, 'Direct'). |
| `distribution_channel` | Categórico | Canal de distribuição da reserva (ex: 'TA/TO' - Agente/Operador de Viagem, 'Direct'). |
| `is_repeated_guest` | Numérico (Binário) | Indica se o hóspede já se hospedou antes (1) ou não (0). |
| `previous_cancellations` | Numérico | Número de reservas anteriores que foram canceladas pelo hóspede. |
| `previous_bookings_not_canceled` | Numérico | Número de reservas anteriores que *não* foram canceladas pelo hóspede. |
| `reserved_room_type` | Categórico | Código do tipo de quarto reservado (ex: 'A', 'C', 'D'). |
| `assigned_room_type` | Categórico | Código do tipo de quarto que foi de fato atribuído ao hóspede. |
| `booking_changes` | Numérico | Número de alterações feitas na reserva desde que foi criada. |
| `deposit_type` | Categórico | Tipo de depósito feito para a reserva (ex: 'No Deposit', 'Refundable'). |
| `agent` | Numérico (ID) | ID da agência de viagens que fez a reserva. (Nulo/0 se foi direta). |
| `company` | Numérico (ID) | ID da empresa que fez a reserva. (Nulo/0 se não foi corporativa). |
| `days_in_waiting_list` | Numérico | Número de dias que a reserva esteve na lista de espera antes de ser confirmada. |
| `customer_type` | Categórico | Tipo de cliente (ex: 'Transient', 'Contract', 'Group'). |
| `adr` | Numérico (Contínuo) | **(Average Daily Rate)** Tarifa Média Diária. Calculada pela divisão da soma de todas as diárias pelo número de noites. |
| `required_car_parking_spaces` | Numérico | Número de vagas de estacionamento solicitadas pelo cliente. |
| `total_of_special_requests` | Numérico | Número de pedidos especiais feitos pelo cliente (ex: cama extra, quarto silencioso). |
| `reservation_status` | Categórico | Status final da reserva (ex: 'Check-Out', 'Canceled', 'No-Show'). |
| `reservation_status_date` | Data | A data em que o `reservation_status` foi definido. |
