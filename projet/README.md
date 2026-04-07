# Langage HitoCrok

**Langage développé par :**

* Jérémy Chény
* Rémy Thibaut

---

## Description du projet

Ce projet consiste à implémenter un **interpréteur pour un mini-langage** en Python.

L’objectif est de recréer certaines fonctionnalités fondamentales d’un langage de programmation :

* gestion de variables
* évaluation d’expressions
* structures de contrôle
* fonctions
* manipulation de chaînes de caractères

L’exécution du programme produit des sorties sur la console préfixées par :

```
HitoCrok >
```

L’arbre de syntaxe abstrait est également affiché sous forme de tuple dans un fichier PDF.

---

## Fonctionnalités implémentées

### 1. Affectations

Possibilité d’affecter une valeur à une variable.

#### Opérations arithmétiques

```
x = 1;

x + 1;
x - 1;
x * 2;
x / 2;      // non absolue
x // 2;     // absolue
x % 2;      // modulo
x ^ 3;      // puissance
```

#### Comparaisons (booléen)

```
x == 1;     // égalité
x != 2;     // différent
x < 5;
x > 0;
x <= 1;
x >= 1;
```

#### Opérateur logiques 
```
(x > 0) && (x < 10);   // ET logique
(x < 0) || (x > 10);   // OU logique
```

---

### 2. Affichage d’expressions numériques

L’instruction `print` permet d’afficher :

* des constantes
* des variables
* des expressions arithmétiques

```
print(1);

x = 1;
print(x);

print(x + 1);
```

---

### 3. Instructions conditionnelles : if / else

Gestion des structures conditionnelles avec ou sans branche `else`.

```
if (1 == 1) {
    print(1);
} else {
    print(2);
};
```

---

### 4. Structures itératives : for / while / do while

#### Boucle for

```
for (i = 1; i < 5; i++) {
    print(i);
};
```

#### Boucle while

```
x = 1;

while (x < 5) {
    print(x);
    x++;
}
```

#### Boucle do while

```
x = 1;

do {
    print(x);
    x++;
} while (x < 10);
```

---

### 5. Gestion des chaînes de caractères

#### Affectation d’une chaîne

```
string = "Hello World!";
```

#### Concaténation

La concaténation entre chaînes et nombres est possible avec gestion de la priorité de type.

```
string = "x";

print(string + "y"); // affiche "xy"
print(string + 1);   // affiche "x1"
print(1 + string);   // affiche 89 (conversion ASCII de "x")
```

#### Affichage de chaînes

```
string = "x";

print(string);

print("Hello World!");
```

---

### 6. Affichage multiple

La fonction `print` accepte plusieurs arguments (numériques ou bien chaînes de caractères).

```
x = 1;
string = "Hello World!";

print(x, string, 1, "Projet");
```

---

### 7. Fonctions void sans arguments

Les fonctions sans valeur de retour peuvent être définies avec ou sans déclaration préalable.

#### Avec déclaration

```
funny x();

print("main");

funny x() {
    print("fonction x");
}
```

#### Sans déclaration

```
print("main");

funny x() {
    print("fonction x");
}
```

---

### 8. Implémentation d'incrémentation et d'affectation élargie

Le langage permet de gérer différents types d'affection / incrémentation pour les variables.

#### Incrémentation / Décrémentation 

```
x = 1;
x++; // Incrémente x de 1 (x vaut 2)
x--; // Décrémente x de 1 (x vaut 1)
```

#### Affectations possibles 

```
x = 1;
x += 2; // Ajoute 2 à x
x -= 2; // Enlève 2 à x
x *= 2; // Multiplie x par 2
x /= 2; // Divise x par 2 (non absolue)
x %= 2; // x vaudra x modulo 2
x //= 2; // Divise x par 2 (absolue)
x ^= 2; // x vaut x puissance 2 (x²)
```


## Fonctionnement de l’interpréteur

L’interpréteur s’appuie sur une fonction principale `evalInst` (non récursive) qui évalue l’arbre de syntaxe abstrait.

Une **pile d’exécution** est utilisée afin de :

* gérer les instructions en cours d’évaluation
* suivre l’ordre d’exécution
* gérer les appels de fonctions

Chaque instruction est ajoutée ou retirée de la pile selon son état d’évaluation.

---

## Exemple d’exécution

```
x = 1;
print(x + 2);
```

Sortie :

```
calc > 3
```

## Prochaines implémentations

Les prochaines implémentations dans le langage sont les suivantes : 
- Gestion des else if (if / else if / else)
- Gestion des appels de fonction avec arguments, retours de valeurs et return coupe circuit;
- Gestion du scope des variables
- Gestion des tableaux et leurs méthodes.
