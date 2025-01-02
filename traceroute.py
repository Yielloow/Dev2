import argparse
import subprocess

def run_traceroute(target, progressive, output_file):
    traceroute_cmd = ["tracert", target]

    if progressive:
        print("\n--- Mode Progressif Activé ---\n")
        process = subprocess.Popen(traceroute_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ""):
            print(line.strip())

    else:
        print("\n--- Mode Standard ---\n")
        result = subprocess.run(traceroute_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)

        if output_file:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(result.stdout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traceroute Tool")
    parser.add_argument("target", type=str, help="URL ou Adresse IP à tracer")
    parser.add_argument("-p", "--progressive", action="store_true", help="Afficher le traceroute en temps réel")
    parser.add_argument("-o", "--output-file", type=str, help="Nom du fichier de sortie pour enregistrer le traceroute")

    args = parser.parse_args()

    try:
        run_traceroute(args.target, args.progressive, args.output_file)
    except Exception as e:
        print(f"Erreur lors de l'exécution du traceroute : {e}")
