namespace DesafioFizzBuzz;

public static class Program
{
    public static void Main()
    {

        for (int i = 0; i < 101; i++)
        {

            string chave = " ";

            if (i != 0)
            {

                if (i % 3 == 0 && i % 5 == 0)
                {

                    chave = "BuzzFizz";

                }

                else if (i % 3 == 0)
                {

                    chave = "Fizz";

                }

                else if (i % 5 == 0)
                {

                    chave = "Buzz";

                }

            }

            Console.Write($"{i} {chave} \n");

        }

        Console.WriteLine("Pressione qualquer tecla para sair...");
        Console.ReadKey();
        
    }
}