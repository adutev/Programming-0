languages = ["Python", "Ruby"]
languages += ["C++", "Java", "C#"]
print(languages)

languages.insert(0, "Haskell")
print(languages)

languages.extend(["Go"])
print(languages)

print(languages[0])
print(languages[1])
print(languages[4])

languages[languages.index("C#")] = "F#"
print(languages)

print(languages[len(languages ) - 1])

print("Haskell" in languages)
print("Ruby" in languages)
print("Go" in languages)
print("Rust" in languages)

