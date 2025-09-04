import os
import subprocess
import sys

MAVEN_PLUGIN = """
<plugin>
  <groupId>org.openrewrite.maven</groupId>
  <artifactId>rewrite-maven-plugin</artifactId>
  <version>5.10.0</version>
  <configuration>
    <activeRecipes>
      <recipe>org.openrewrite.java.testing.junit5.JUnit4to5Migration</recipe>
    </activeRecipes>
  </configuration>
</plugin>
"""

GRADLE_PLUGIN = """
plugins {
    id("org.openrewrite.rewrite") version("6.3.4")
}

rewrite {
    activeRecipe("org.openrewrite.java.testing.junit5.JUnit4to5Migration")
}
"""

def is_maven_project():
    return os.path.isfile("pom.xml")

def is_gradle_project():
    return os.path.isfile("build.gradle") or os.path.isfile("build.gradle.kts")

def update_maven_pom():
    with open("pom.xml", "r", encoding="utf-8") as f:
        content = f.read()

    if "<artifactId>rewrite-maven-plugin</artifactId>" in content:
        print("🔄 Plugin OpenRewrite já está presente no pom.xml")
        return

    if "<plugins>" in content:
        content = content.replace("<plugins>", f"<plugins>{MAVEN_PLUGIN}")
    else:
        # Tenta adicionar dentro do <build>
        content = content.replace("</build>", f"<plugins>{MAVEN_PLUGIN}</plugins></build>")

    with open("pom.xml", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Plugin OpenRewrite adicionado ao pom.xml")

def update_gradle_build():
    gradle_file = "build.gradle.kts" if os.path.isfile("build.gradle.kts") else "build.gradle"
    with open(gradle_file, "r", encoding="utf-8") as f:
        content = f.read()

    if "org.openrewrite.rewrite" in content:
        print(f"🔄 Plugin OpenRewrite já está presente no {gradle_file}")
        return

    content = GRADLE_PLUGIN + "\n" + content

    with open(gradle_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Plugin OpenRewrite adicionado ao {gradle_file}")

def run_maven_migration():
    print("▶️ Executando a migração com Maven...")
    subprocess.run(["mvn", "rewrite:run"], check=True)

def run_gradle_migration():
    print("▶️ Executando a migração com Gradle...")
    subprocess.run(["./gradlew", "rewriteRun"], check=True)

def run(metadata):
    if is_maven_project():
        print("🛠️ Projeto Maven detectado.")
        update_maven_pom()
        run_maven_migration()

    elif is_gradle_project():
        print("🛠️ Projeto Gradle detectado.")
        update_gradle_build()
        run_gradle_migration()

    else:
        print("❌ Nenhum projeto Maven ou Gradle detectado neste diretório.")
        sys.exit(1)
