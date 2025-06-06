using System;

namespace TemperatureConverter
{
    class Program
    {
        public static void Main()
        {
            int fahrenheit = 94;
            decimal celsius = (fahrenheit - 32m) * (5m / 9m);

            Console.WriteLine($"Temperatura em Fahrenheit: {fahrenheit}°F");
            Console.WriteLine($"Temperatura convertida para Celsius: {Math.Round(celsius, 2)}°C");
        }
    }
}