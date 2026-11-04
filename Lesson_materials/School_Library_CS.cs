#nullable enable
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;

// In a C# console project, use this file instead of the default Program.cs.
// Put the existing books.json in the working directory (the project folder
// when running dotnet run). Requires .NET 6 or later.
class Book
{
    [JsonPropertyName("title")]
    public string Title { get; set; } = "";

    [JsonPropertyName("borrowed_by")]
    public string? BorrowedBy { get; set; }
}

class Program
{
    static readonly string FilePath = Path.Combine(Directory.GetCurrentDirectory(), "books.json");
    static Dictionary<string, Book> books = new Dictionary<string, Book>();

    static string Input(string prompt)
    {
        Console.Write(prompt);
        return (Console.ReadLine() ?? "").Trim();
    }

    static Dictionary<string, Book> LoadBooks()
    {
        string json = File.ReadAllText(FilePath);
        return JsonSerializer.Deserialize<Dictionary<string, Book>>(json)
            ?? throw new InvalidDataException("books.json must contain a book dictionary.");
    }

    static void SaveBooks()
    {
        string json = JsonSerializer.Serialize(books, new JsonSerializerOptions
        {
            WriteIndented = true
        });
        File.WriteAllText(FilePath, json);
    }

    static void ShowBooks()
    {
        Console.WriteLine("\n--- LIBRARY BOOKS ---");
        foreach (var entry in books)
        {
            string bookId = entry.Key;
            Book book = entry.Value;
            string status = book.BorrowedBy is null
                ? "Available" : "Borrowed by " + book.BorrowedBy;
            Console.WriteLine($"{bookId} - {book.Title} - {status}");
        }
    }

    static void AddBook()
    {
        string title = Input("Book title: ");
        if (title == "")
        {
            Console.WriteLine("Title cannot be empty.");
            return;
        }
        string bookId = (books.Keys.Select(int.Parse).DefaultIfEmpty(0).Max() + 1).ToString();
        books[bookId] = new Book { Title = title, BorrowedBy = null };
        SaveBooks();
        Console.WriteLine("Book added!");
    }

    static void BorrowBook()
    {
        ShowBooks();
        string bookId = Input("Book ID: ");
        if (!books.ContainsKey(bookId))
            Console.WriteLine("Book does not exist.");
        else if (books[bookId].BorrowedBy is not null)
            Console.WriteLine("Book is already borrowed.");
        else
        {
            string name = Input("Student name: ");
            if (name == "")
            {
                Console.WriteLine("Name cannot be empty.");
                return;
            }
            books[bookId].BorrowedBy = name;
            SaveBooks();
            Console.WriteLine("Book borrowed!");
        }
    }
