using System;
using System.Linq;

namespace DesafioFizzBuzz;

public static class Program
{
    public static void Main()
    {
        Random random = new Random();
        int current = 0;

        do
        {
            current = random.Next(1, 11);
            Console.WriteLine(current);
        } while (current != 7);
    }

}