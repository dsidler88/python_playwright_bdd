@hotlink @Discovery
Feature: As a new-monitor user,I can discovery snmp resources.

  Background: 
    Given I has logged in

  Scenario Outline: I can discovery snmp resources
    When I wants to add snmp connection <connection_name> <port> <community>
    Then I should see <connection_name> in snmp connection list
    And I can delete snmp connection <connection_name>

    Examples: 
      | connection_name   | port  | community |
      | snmp_connection_1 |   161 | xxxxx     |
      | vsu_connection_1  | 20003 | xxxxx     |
