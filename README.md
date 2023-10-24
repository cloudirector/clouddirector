```elixir
defmodule Cloudirector do
  @website "https://cloudirector.github.io/"
  defstruct experience: nil
  def new do
    %Cloudirector{}
  end
  def say_hello(%Cloudirector{} = me) do
    IO.puts("wsp nerds go look at my spaghetti code")
    me
  end
  def open_website(%Cloudirector{website: website} = me) do
    System.cmd("/bin/chromium", [website])
    me
  end
end
me = %Cloudirector{}
me = Cloudirector.say_hello(me)
me = Cloudirector.open_website(me)
```
