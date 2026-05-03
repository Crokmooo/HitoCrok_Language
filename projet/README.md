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

#### Opérateurs logiques 
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

### 3. Instructions conditionnelles : if / else / else if 

Gestion des structures conditionnelles avec ou sans branche `else`.

```
if (1 == 2) {
    print(1);
} else if (1 == 1) {
    print(2);
} else {
    print(3);
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
print(1 + string);   // affiche 121 (conversion ASCII de "xy")
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

### 8. Fonction avec arguments et retour coupe circuit


#### Avec arguments
```
funny x(string);

print(x("hello")); // Affiche hello

funny x(string) {
    return string;
}
```

#### Avec plusieurs return

```
funny x(number);

print(x(1)); // Affiche hello
print(x(2)); // Affiche world

funny x(number) {
    if (number == 1) {
        return "hello;
    }
    return "world";
}
```

#### Fonctions récursives

```
funny x(number);

print(x(1)); // Affiche hello
print(x(2)); // Affiche world

funny x(number) {
    if (number == 1) {
        return "hello;
    }
    return "world";
}
```
---

#### Fonctions récursives terminales optimisées

Notre langage permet d'optimiser l'exécution d'une fonction récursive terminale.

```
print(fact(5, 1));

funny fact(n, acc) {
    if (n == 0) {
        return acc;
    };
    return fact(n-1, n*acc);
}
```

Pour qu'une fonction récursive soit terminale, son dernier return doit obligatoirement être un appel à elle-même uniquement (pas d'expression).
Ainsi, l'exécution de la fonction peut être faite grâce à une boucle, limitant la taille de la pile.


### 9. Implémentation d'incrémentation et d'affectation élargie

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

---

### 10. Fonctions Scan

Notre langage propose deux fonctions pour scanner ce que l'utilisateur écrira dans le terminal : 
- **sananes()** récupérant la valeur pour l'exploiter comme une expression
- **trancho()** récupérant un programme exécuté à la volée, pouvant avoir un impact sur le reste de l'exécution.

#### Fonction Sananes

**sananes()** est l'équivalent d'un **input()** ou d'un **scanf()**.\


```
x = sananes();
// Utilisateur écrit 1+1
print(x); // Affiche 2

y = sananes();
// Utilisateur écrit "Hello World!"
print(y); // Affiche Hellow World!

```

#### Fonction Trancho

**trancho()** génère un nouvel arbre AST passant dans evalInst avec sa propre pile, mais en ayant accès aux fonctions définis ainsi qu'aux variables (des différents scopes précédemment créés).

```
x = 1;
trancho();
// Utilisateur écrit x=2;
print(x); // Affiche 2 et non 1 (x a été mis à jour).
```

```
funny x();

x = 1;
trancho();
// Utilisateur écrit x();x+=1;

// Affiche "hello world!"
print(x); // Affiche 2 et non 1 (x a été mis à jour).

funny x(){
    print("hello world!");
}
```

### 

---

### 11. Gestion des tableaux 

Notre langage propose une gestion des tableaux (une ou plusieurs dimensions).
Un tableau ne peut posséder qu'un seul type : celui de son premier élément (en profondeur si plusieurs dimensions)

```
tab = [1,2]; // tab est un tableau de 2 éléments : 1 et 2
tab2 = [[1,2], [1,2]]; // tab est un tableau à deux dimensions
tab3 = ["a", 1]; // n'est pas possible
```

Il est possible d'accéder à un élément du tableau sur une ou plusieurs dimensions :

```
tab = [1,2];
x = tab[0]: // x vaut 1

tab2 = [[1,2], [1,2]];
x = tab[0]; // x vaut [1,2]
y = tab[0][0]; // y vaut 1
z = x[0]; // z vaut 1 
```

#### Méthodes disponibles sur les tableaux

##### 1. Push 

La méthode push permet d'ajouter un élément au tableau (argument obligatoire) : 

```
tab = [1,2];
tab.push(1);
print(tab); // Affiche [1, 2, 1]
```

```
tab = [[1,2], [1,2]];
tab.push(1);
print(tab); // Affiche [[1, 2], [1, 2], 1]
```

##### 2. Pop

La méthode pop permet de retirer le dernier élément du tableau (aucun argument) :

```
tab = [1,2];
tab.pop();
print(tab); // Affiche [1]
```

```
tab = [[1,2], [1,2]];
tab.pop();
print(tab); // Affiche [[1, 2]]
```

##### 3. Remove

La méthode remove permet de retirer l'élément du tableau à un index précis (avec un argument) :

```
tab = [1,2,3];
tab.remove(1);
print(tab); // Affiche [1,3]
```

```
tab = [[1,2], [3,4], [5,6]];
tab.remove(1);
print(tab); // Affiche [[1, 2], [5, 6]]
```

##### 4. Show

La méthode show permet d'afficher le contenu d'un tableau comme un print : 

```
tab = [1,2,3];
tab.show(); // Affiche [1, 2, 3]
```

##### 5. Size

La méthode size d'obtenir la taille du tableau (sur la première dimension) :

```
tab = [1,2,3];
print(tab.size()); // Affiche 3
```

### 12. Commentaires

Il est possible d'écrire des commentaires dans le code. Les commentaires sont multi-lignes. 

```
/*
Lorem
Ipsum
*/
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
HitoCrok > 3
```
