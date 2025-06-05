using System;
using System.Linq;

namespace Csharp_For;

public static class Program
{
    public static void Main()
    {

        //Contagem progressiva
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(i);
        }

        Console.WriteLine("\n");

        //Contagem regressiva
        for (int i = 10; i >= 0; i--)
        {
            Console.WriteLine(i);
        }

        Console.WriteLine("\n");

        //Pare no 7:

        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(i);
            if (i == 7) break;
        }

        Console.WriteLine("\n");

        //Matriz

        string[] names1 = { "Alex", "Eddie", "David", "Michael" };
        for (int i = names1.Length - 1; i >= 0; i--)
        {
            Console.WriteLine(names1[i]);
        }

        Console.WriteLine("\n");

        //Diferença ao foreach

        //Errado

        // string[] names = { "Alex", "Eddie", "David", "Michael" };
        // foreach (var name in names)
        //{

        //    if (name == "David") name = "Sammy";
        //}

        //Correto:

        // string[] names = { "Alex", "Eddie", "David", "Michael" };
        //for (int i = 0; i < names.Length; i++)
        // if (names[i] == "David") names[i] = "Sammy";

        //foreach (var name in names) Console.WriteLine(name);

        string[] names = { "Alex", "Eddie", "David", "Michael" };

        for (int i = 0; i < names.Length; i++)
        {
            if (names[i] == "David")
            {
                names[i] = "Sammy";
            }
        }

        foreach (var name in names)
        {
            Console.WriteLine(name);
        }

    }
}