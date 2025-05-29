using System;

namespace RolagemDeDados
{
    class Program
    {
        public static void Main()
        {
            // Teste Upper case
            string teste = "Rolagem de dados".ToUpper();
            Console.WriteLine(teste);
            Console.WriteLine();

            // Rolagem dado:
            Random dice = new Random();
            int rollD6 = dice.Next(1, 7);
            Console.WriteLine($"O número sorteado pelo D6 foi: {rollD6}");

            // Rolagem Tripla:
            int rollD8 = dice.Next(1, 9);
            int rollD12 = dice.Next(1, 13);
            int rollD20 = dice.Next(1, 21);

            Console.WriteLine($"O número sorteado pelo D8 foi: {rollD8}");
            Console.WriteLine($"O número sorteado pelo D12 foi: {rollD12}");
            Console.WriteLine($"O número sorteado pelo D20 foi: {rollD20}");

            // Bigger value desafio (minha solução):
            int firstValue = 500;
            int secondValue = 600;
            int largerValue;

            if (firstValue > secondValue)
            {
                largerValue = firstValue;
            }
            else
            {
                largerValue = secondValue;
            }

            Console.WriteLine($"Minha solução {largerValue}");

            // Solução Microsoft:
            int firstValue2 = 500;
            int secondValue2 = 600;
            int largerValue2 = Math.Max(firstValue2, secondValue2);
            Console.WriteLine($"Solução Microsoft Learn: {largerValue2}");
        }
    }
}