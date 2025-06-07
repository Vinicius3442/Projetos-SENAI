// program em que o desafio é corrigir a indentação do código
// e melhorar a legibilidade do código, mantendo a lógica intacta
namespace Csharp_Corrijirindentacao;

public static class Program
{
    public static void Main()
    {

        int[] numbers = { 4, 8, 15, 16, 23, 42 };

        bool found = false;

        int total = 0;

        foreach (int number in numbers)
        {
            total += number;

            if (number == 42) { found = true; }

        }

        if (found) { Console.WriteLine("Set contains 42"); }

        Console.WriteLine($"Total: {total}");
    }
}