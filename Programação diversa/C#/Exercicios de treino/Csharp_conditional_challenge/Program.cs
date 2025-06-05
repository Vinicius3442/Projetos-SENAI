using System;
using System.Linq;

namespace Csharp_conditional_challenge;

public static class Program
{
    public static void Main()
    {
        Console.WriteLine("Digite seu nivel de permissão: ");
        string? permission1 = Console.ReadLine();

        Console.WriteLine("Digite seu nivel:");

        string permission = char.ToUpper(permission1[0]) + permission1.Substring(1);

        int level = Convert.ToInt32(Console.ReadLine());

        bool admin = permission.Contains("Admin");

        bool manager = permission.Contains("Manager");

        if (admin == true && level > 55)
        {

            Console.Write("Welcome, Super Admin user.");
            
        }
        else if (admin == true && level <= 55)
        {

            Console.Write("Welcome, Admin user.");

        }
        else if (manager == true && level >= 20)
        {

            Console.Write("Contact an Admin for access.");


        }
        else if (manager == true && level < 20)
        {

            Console.Write("You do not have sufficient privileges.");

        }
        else
        {

            Console.Write("You do not have sufficient privileges.");

        }

    }
}