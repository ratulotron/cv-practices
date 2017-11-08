defmodule RandomGenerator do
  @moduledoc """
  Documentation for RandomGenerator.
  """

  @doc """
  Hello world.

  ## Examples

      iex> RandomGenerator.hello
      :world

  """
  def hello do
    :world
  end

  def show_chars(characters) do
    characters 
      |> Enum.join(" ")
      |> IO.puts
  end

  def create_line(characters, line_length) do
    Stream.repeatedly(fn -> Enum.random(characters) end)
    |> Enum.take(line_length)
    |> Enum.join(" ")
  end

  def create_paragraph(characters, line_length, paragraph_length) do
    
  end

  def main do
    characters = [
      "□", 
      "■", 
      "△", 
      "▲", 
      "⬡", 
      "⬢", 
      "○", 
      "●"
      # "a", 
      # "b", 
      # "c", 
      # "d", 
      # "e", 
      # "f", 
      # "g", 
      # "h"
    ]
    # show_chars(characters)
    # characters |> Enum.random |> IO.puts
    characters |> create_line(5) |> IO.puts
  end

  # def random_character(characters) do
  #   random_number = characters |> length |> :rand.uniform
  #   Enum.at(characters, random_number)
  # end

  # def create_line(string \\ "", characters, length) do
  #   if length == 1 do
  #     string <> random_character(characters)
  #   else
  #     char = random_character(characters)
  #     string = string <> char
  #     create_line(string , characters, length - 1)
  #   end
  # end


  # def main do
  #   create_line("", characters, 5) |> IO.puts
  # end
end

RandomGenerator.main()