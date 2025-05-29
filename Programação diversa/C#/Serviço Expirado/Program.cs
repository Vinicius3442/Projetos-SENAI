using System;

namespace SubscriptionReminder
{
    class Program
    {
        public static void Main()
        {
            Random random = new Random();
            int daysUntilExpiration = random.Next(12); // Gera um valor de 0 a 11
            int discountPercentage = 0;

            Console.WriteLine($"Dias até expiração: {daysUntilExpiration}\n");

            if (daysUntilExpiration <= 10 && daysUntilExpiration > 5)
            {
                Console.WriteLine("Your subscription will expire soon. Renew now!");
            }
            else if (daysUntilExpiration <= 5 && daysUntilExpiration > 1)
            {
                discountPercentage = 10;
                Console.WriteLine($"Your subscription expires in {daysUntilExpiration} days.");
                Console.WriteLine($"Renew now and save {discountPercentage}%!");
            }
            else if (daysUntilExpiration == 1)
            {
                discountPercentage = 20;
                Console.WriteLine("Your subscription expires within a day!");
                Console.WriteLine($"Renew now and save {discountPercentage}%!");
            }
            else if (daysUntilExpiration == 0)
            {
                Console.WriteLine("Your subscription has expired.");
            }
        }
    }
}