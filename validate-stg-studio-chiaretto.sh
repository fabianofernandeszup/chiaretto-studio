#!/bin/bash

# Diretório base onde os diretórios actions, plugins e stacks estão localizados
BASE_DIR="./"

# Função para publicar o plugin
validate_plugin() {
    local dir=$1
    if [ -f "$dir/plugin.yaml" ]; then
        echo "Publicando plugin na pasta: $dir"
        (cd "$dir" && stk-stg validate plugin )
    fi
}

# Função para publicar a action
validate_action() {
    local dir=$1
    if [ -f "$dir/action.yaml" ]; then
        echo "Publicando action na pasta: $dir"
        (cd "$dir" && stk-stg validate action )
    fi
}

# Função para publicar a stack
validate_stack() {
    local dir=$1
    if [ -f "$dir/stack.yaml" ]; then
        echo "Publicando stack na pasta: $dir"
        (cd "$dir" && stk-stg validate stack )
    fi
}

# Função para percorrer os diretórios e subdiretórios
process_directory() {
    local base_dir=$1
    for dir in "$base_dir"/*/; do
        validate_plugin "$dir"
        validate_action "$dir"
        validate_stack "$dir"
    done
}

# Processa os diretórios actions, plugins e stacks
process_directory "$BASE_DIR/actions"
process_directory "$BASE_DIR/plugins"
process_directory "$BASE_DIR/stacks"