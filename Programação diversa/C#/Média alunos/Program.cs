using System;

namespace CalculoDeMedias
{
    class Program
    {
        public static void Main()
        {
            int numNotas = 5;

            // Notas de Sophia
            int sophia1 = 93, sophia2 = 87, sophia3 = 98, sophia4 = 95, sophia5 = 100;
            // Notas de Nicolas
            int nicolas1 = 80, nicolas2 = 83, nicolas3 = 82, nicolas4 = 88, nicolas5 = 85;
            // Notas de Zahirah
            int zahirah1 = 84, zahirah2 = 96, zahirah3 = 89, zahirah4 = 85, zahirah5 = 79;
            // Notas de Jeong
            int jeong1 = 90, jeong2 = 92, jeong3 = 98, jeong4 = 100, jeong5 = 97;

            // Cálculo das médias
            decimal sophiaMedia = (sophia1 + sophia2 + sophia3 + sophia4 + sophia5) / (decimal)numNotas;
            decimal nicolasMedia = (nicolas1 + nicolas2 + nicolas3 + nicolas4 + nicolas5) / (decimal)numNotas;
            decimal zahirahMedia = (zahirah1 + zahirah2 + zahirah3 + zahirah4 + zahirah5) / (decimal)numNotas;
            decimal jeongMedia = (jeong1 + jeong2 + jeong3 + jeong4 + jeong5) / (decimal)numNotas;

            // Exibição dos resultados
            Console.WriteLine($"A nota de Sophia foi: {sophiaMedia}");
            Console.WriteLine($"A nota de Nicolas foi: {nicolasMedia}");
            Console.WriteLine($"A nota de Zahirah foi: {zahirahMedia}");
            Console.WriteLine($"A nota de Jeong foi: {jeongMedia}");
        }
    }
}