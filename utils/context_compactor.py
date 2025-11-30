try:
    from llm import llm_call
    HAS_LLM = True
except (ImportError, ModuleNotFoundError):
    HAS_LLM = False


def summarize_text(text: str, max_tokens: int = 512) -> str:
    """Summarize text using LLM if available, otherwise return a simple summary."""
    if HAS_LLM:
        try:
            prompt = (
                f"You are a concise code summarizer. Summarize the important design choices, functions, and possible issues in the following code. "
                f"Be direct and output a bullet list.\n\nCODE:\n{text}"
            )
            resp = llm_call(prompt, max_output_tokens=max_tokens)
            return resp
        except Exception:
            # Fall through to simple summary if LLM call fails
            pass
    
    # Simple fallback summary
    lines = text.split('\n')
    functions = [line for line in lines if 'def ' in line]
    return f"Code summary: {len(lines)} lines, {len(functions)} function(s) defined."


def compact_files(file_texts: dict, max_chars: int = 2000) -> str:
    # file_texts: {path: content}
    # naive compaction: summarize largest files until under budget
    combined = "\n\n".join([f"FILE: {p}\n{t[:2000]}" for p, t in file_texts.items()])
    if len(combined) <= max_chars:
        return combined
    return summarize_text(combined, max_tokens=512)
