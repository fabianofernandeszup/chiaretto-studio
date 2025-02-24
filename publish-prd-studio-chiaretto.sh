#!/bin/bash

# Diretório base onde os diretórios actions, plugins e stacks estão localizados
BASE_DIR="./"
# Nome do estúdio para publicação
STUDIO_NAME="chiaretto-studio"

# Função para publicar o plugin
publish_plugin() {
    local dir=$1
    if [ -f "$dir/plugin.yaml" ]; then
        echo "Publicando plugin da pasta: $dir"
        (cd "$dir" && stk publish plugin --studio "$STUDIO_NAME")
    fi
}

# Função para publicar a action
publish_action() {
    local dir=$1
    if [ -f "$dir/action.yaml" ]; then
        echo "Publicando action da pasta: $dir"
        (cd "$dir" && stk publish action --studio "$STUDIO_NAME")
    fi
}

# Função para publicar o workflow
publish_workflow() {
    local dir=$1
    if [ -f "$dir/workflow.yaml" ]; then
        echo "Publicando workflow da pasta: $dir"
        (cd "$dir" && stk publish stack --studio "$STUDIO_NAME")
    fi
}

# Função para publicar a stack
publish_stack() {
    local dir=$1
    if [ -f "$dir/stack.yaml" ]; then
        echo "Publicando stack da pasta: $dir"
        (cd "$dir" && stk publish stack --studio "$STUDIO_NAME")
    fi
}

# Função para percorrer os diretórios e subdiretórios
process_directory() {
    local base_dir=$1
    for dir in "$base_dir"/*/; do
        publish_plugin "$dir"
        publish_action "$dir"
        publish_workflow "$dir"
        publish_stack "$dir"
    done
}

# Processa os diretórios actions, plugins, workflows e stacks
process_directory "$BASE_DIR/actions"
process_directory "$BASE_DIR/plugins"
process_directory "$BASE_DIR/workflow"
process_directory "$BASE_DIR/stacks"