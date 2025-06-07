namespace Cara_coroa;

public static class Program
{
    public static void Main()
    {
        Console.WriteLine("Jogo Cara ou Coroa");
        Console.WriteLine("Pressione Enter para jogar...");
        Console.Read();
        
        Random random = new Random();

        int lancamento = random.Next(1, 3);

        Console.Write($"Lançamento {(lancamento == 2 ? "Coroa" : "Cara")}");
    }
}