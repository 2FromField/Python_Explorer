// Java est un langage orienté objet, tu écris du code .java, il est compilé en bytecode
// et exécuté par la JVM (Java Virtual Machine). Résultat : le même
// programme peut tourner sur Windows/MacOS/Linux si la JVM est installée

// Pour run un programme:
// 1) compiler le fichier : `javac Main.java`
// 2) run : `java Main`
import java.util.ArrayList;

// POO : classe, objet, constructeur
class Player {
    String name;
    int age;

    Player(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void sayHello() {
        System.out.println("Salut, je suis " + name);
    }
}

public class Main {
    // Fonctions
    public static int addition(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        // class Main : une classe (obligatoire)
        // main : point d'entrée du programme
        // System.out.println : affiche une ligne

        int age = 25;
        double taille = 1.82;
        boolean ok = true;
        char lettre = 'T';
        String nom = "Mario";

        // Concaténer les strings:
        System.out.println("Nom: " + nom + ", âge: " + age);

        // Conditions "classique"
        if (taille >= 1.80) {
            System.out.println("Taille réglementaire");
        } else {
            System.out.println("Taille invalide");
        }

        // Conditions "switch" (cas multiples)
        switch (lettre) {
            case 'A':
                System.out.println("Lettre A");
                break;
            case 'B':
                System.out.println("Lettre B");
                break;

            default:
                System.out.println("Autre lettre que 'A' et 'B'");
                break;
        }

        // Boucles "for"
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        // Boucles "While"
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }

        // For-each (pour tableaux-listes)
        int[] notes = { 10, 14, 8 };
        for (int n : notes) {
            System.out.println(n);
        }

        // Utilisation de la fonctions "addition"
        int r = addition(2, 3);
        System.out.println(r);

        // Tableau
        int[] t = new int[3];
        t[0] = 5;
        System.out.println(t);

        // List
        String[] noms = { "Nadal", "Federer" };
        for (String n : noms) {
            System.out.println(n);
        }

        ArrayList<String> joueurs = new ArrayList<>();
        joueurs.add("Nadal");
        joueurs.add("Federer");
        System.out.println(joueurs.get(0));

        // Appel de la classe "Player"
        Player p = new Player("Matéo", 20);
        p.sayHello();

        // Try / except
        try {
            int x = Integer.parseInt(("abc"));
        } catch (NumberFormatException e) {
            System.out.println("Pas un nombre");
        }
    }
}
