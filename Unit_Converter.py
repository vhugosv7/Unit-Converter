'''You are required to build a program that can convert between
different units of measurement.
It can convert units of length, weight, temperature. The user can input a
value and select the units to convert from and to.
The program will then display the converted value.'''
from pint import UnitRegistry


def Length_conversion() -> str:
    print('-> Length conversion')
    value = float(input("Value:"))
    from_unit = input('''Type the unit of the value:
                           - millimeter
                           - centimeter
                           - meter
                           - kilometer
                           - inch
                           - foot
                           - yard
                           - mile: ->''')

    to_unit = input('''Converts to:
                           - millimeter
                           - centimeter
                           - meter
                           - kilometer
                           - inch
                           - foot
                           - yard
                           - mile: ->''')

    try:

        # The UnitRegistry stores the unit definitions.
        ureg = UnitRegistry()
        # Combine the user value and it's initial unit.
        value_unit = str(value) + " " + from_unit
        # Unit conversion
        converted_value = ureg.Quantity(value_unit).to(to_unit)
        print("Orginal value: ", value_unit)
        print("Result", converted_value)

    except Exception:
        print('''Can't convert. Make sure tu select a valid unit:
              - millimeter
              - centimeter
              - meter
              - kilometer
              - inch
              - foot
              - yard
              - mile
              ''')


def Weight_conversion() -> str:
    print("-> Weight conversion")
    value = float(input("Value:"))
    from_unit = input('''Type the unit of the value:
                           - milligram
                           - gram
                           - kilogram
                           - ounce
                           - pound: ->''')

    to_unit = input('''Converts to:
                           - milligram
                           - gram
                           - kilogram
                           - ounce
                           - pound: ->''')

    try:

        ureg = UnitRegistry()
        # Combine the user value and it's initial unit. Ex=45.5 gram.
        conversion = str(value) + " " + from_unit
        # Unit conversion
        converted_value = ureg.Quantity(conversion).to(to_unit)
        print("Orginal value: ", conversion)
        print("Result", converted_value)

    except Exception:
        print('''Can't convert. Make sure tu select a valid unit:
              - milligram
              - gram
              - kilogram
              - ounce
              - pound:
              ''')


def Temperature_conversion() -> str:
    print("-> Temperature conversion")
    # Getting yhe inital and requested values from the user
    value = float(input("Value:"))
    from_unit = input('''Type the unit of the value:
                           - Celsius
                           - Fahrenheit
                           - Kelvin: ->''').capitalize()

    to_unit = input('''Converts to:
                           - Celsius
                           - Fahrenheit
                           - Kelvin: ->''').capitalize()

    # The UnitRegistry stores the unit definitions.
    ureg = UnitRegistry()
    # Getting only 3 numbers after the point
    ureg.formatter.default_format = '.3f'

    # Options to convert temperature
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        conversion_from = ureg.Quantity(value, ureg.degC)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('degF'))

    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        conversion_from = ureg.Quantity(value, ureg.degF)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('degC'))

    elif from_unit == "Celsius" and to_unit == "Kelvin":
        conversion_from = ureg.Quantity(value, ureg.degC)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('kelvin'))

    elif from_unit == "Kelvin" and to_unit == "Celsius":
        conversion_from = ureg.Quantity(value, ureg.degC)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('degC'))

    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        conversion_from = ureg.Quantity(value, ureg.degC)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('degC'))

    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        conversion_from = ureg.Quantity(value, ureg.degC)
        print("Original value: ", str(value) + from_unit)
        print("Result: ", conversion_from.to('degC'))

    elif from_unit == to_unit:
        print("Same unit", value, from_unit, to_unit)

    else:
        print("Failed. Make sure to select a valid unit.")


def conversion():
    # Request the conversion type from the user.
    conversion_type = int(input('''Number of the option you want to select:
                             1.- 📏 Length
                             2.- 🪨  Weight
                             3.- 🌡️  Temperature
                             -> '''))

    if conversion_type == 1:
        Length_conversion()

    elif conversion_type == 2:
        Weight_conversion()

    elif conversion_type == 3:
        Temperature_conversion()
    else:
        print("Unknown option, try again")


conversion()
