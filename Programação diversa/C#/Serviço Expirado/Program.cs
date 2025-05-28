Random random = new Random();
int daysUntilExpiration = random.Next(12);
int discountPercentage = 0;

if (daysUntilExpiration <= 10 && daysUntilExpiration > 5)
{
    Console.Write("Your subscription will expire soon. Renew now!");
}

else if (daysUntilExpiration <= 5 && daysUntilExpiration > 1)
{
    discountPercentage = 10;
    Console.Write($"Your subscription expires in {daysUntilExpiration} days. \nRenew now and save {discountPercentage}%");
}

else if (daysUntilExpiration == 1)
{
    discountPercentage = 20;
    Console.Write($"Your subscription expires within a day! \nRenew now and save {discountPercentage}%!");
}

else if (daysUntilExpiration == 0)
{
    Console.Write($"Your subscription has expired.");
}