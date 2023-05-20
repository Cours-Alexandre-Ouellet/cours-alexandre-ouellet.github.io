# Déclaration de types

Kotlin est un langage orienté objet fortement typé. Il support aussi la programmation procédurale sans classe. Ce sujet sera couvert dans une autre leçon. 

Une classe en Kotlin se déclare avec le mot-clé **class** suivi du nom de celle-ci. La convention de nomenclature veut que le nom soit en *CamelCase*. La visibilité par défaut des types est **public**, donc il n'est pas nécessaire de l'indiquer.

```kotlin
class Chat {
  // Contenu de la classe
}
```

## Propriétés

La classe peut ensuite définir des propriétés. Celles-ci peuvent être déclarés de plusieurs façons selon l'utilisation et leur méthode d'initialisation.

D'abord, on peut déclarer une propriété qui pourra être modifiée (muable) à tout moment par le mot-clé **var** ou une propriété en lecture seule (immuable) par le mot-clé **val**. Le type doit être indiqué, à moins qu'il ne puisse être déduit à l'initialisation. Un type indiqué qui peut être déduit provoque un avertissement, mais pas d'erreur. Par défaut, les propriétés sont publiques, mais on peut indiquer **protected** ou **private** pour en réduire la portée.

```kotlin
class Chat {
    private val nom : String = "M. Moustache"   // Le nom ne change jamais
    private var age : Int = 5   // L'âge peut être modifiée
}
```

Les propriétés doivent toujours être assignés avant la fin de l'exécution du constructeur, sans quoi une erreur est levée. Pour éviter une erreur, la propriété **lateinit** doit être ajoutée à la déclaration de la propriété.

```kotlin
class Chat {
    private val nom : String = "M. Moustache"
    private var age : Int = 5
    private lateinit var couleur : String   // Peut être préciser après l'initialisation, attention aux erreurs
}
```

### Accesseur et mutateurs

Par défaut, les propriétés déclarés avec **var** définissent un accesseur et un mutateur tandis que les propriétés déclarées avec **val** définissent uniquement un accesseur.

Il est possible de modifier le comportement par défaut des accesseurs et des mutateurs par la syntaxe suivante.

```kotlin
class Chat {
    private val nom : String = "M. Moustache"
    private var age : Int = 5
        get() =      // code de l'accesseur
        set(value) = // code du mutateur

    private lateinit var couleur : String
}
```

## Constructeurs

Les classes dans Kotlin définissent un constructeur primaire directement dans la déclaration de la classe et des constructeurs secondaires au besoin. Le constructeur primaire ne peut pas contenir d'instruction, il peut seulement définir des paramètres. Il n'est pas nécessaire d'utiliser la référence **this** lorsqu'on assigne des valeurs à partir du constructeur.

```kotlin
class Chat constructor(nom: String, age:Int) {
    private val nom : String = nom
    private var age : Int = age
    private lateinit var couleur : String
}
```

Le mot-clé constructor peut être omit si aucune annotation n'y est attachée. 

Les constructeurs secondaires prennent la forme de bout de code dans un bloc **init**. Il peut y avoir plusieurs blocs **init** qui sont exécutés dans l'ordre de la définition de la classe.

```kotlin
class Chat(nom: String, age:Int) {
    private val nom : String = nom
    private var age : Int = age
    private lateinit var couleur : String

    init {
        couleur = 'Rose'
    }
}
```

Il est aussi possible de définir les propriétés directement dans la définition du constructeur primaire. Évidemment, les propriétés **lateinit** n'y sont pas déclarés. La classe ci-dessous est identique à la classe Chat déclaré à l'exemple précédent.

```kotlin
class Chat(val nom:String, var age:Int) {
    private lateinit var couleur : String
}
```

## Méthodes

Les méthodes d'une classe sont déclarées par le mot-clé **fun**


### Documentation

https://kotlinlang.org/docs/classes.html#constructors
