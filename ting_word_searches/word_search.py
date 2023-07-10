def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data["nome_do_arquivo"]
        file_lines = file_data["linhas_do_arquivo"]
        occurrences = []

        for line, content in enumerate(file_lines, 1):
            if word.lower() in content.lower():
                occurrences.append({"linha": line})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    for index in range(0, len(instance)):
        file_data = instance.search(index)
        file_name = file_data["nome_do_arquivo"]
        file_lines = file_data["linhas_do_arquivo"]
        occurrences = []

        for line, content in enumerate(file_lines, 1):
            if word.lower() in content.lower():
                occurrences.append({"linha": line, "conteudo": content})
        
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result
