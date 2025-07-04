import re 

def remove_punctuation(text):
    """
    """
    return re.sub(r'[^\w\s]', '', text)

def remove_numbers(text):
    """
    """
    return re.sub(r'\d+', '', text)

def remove_extra_spaces(text):
    """
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_diacritics(text):
    """
    """
    return re.sub(r'[\u064b-\u0652]', '', text)

def unify_arabic_characters(text):
    """
    """
    text = re.sub(r'[أإآ]', 'ا', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ى', 'ي', text)
    return text

def clean_and_normalize_arabic_text(text):
    """
    """
    text = remove_diacritics(text)
    text = unify_arabic_characters(text)
    text = remove_punctuation(text)
    text = remove_numbers(text) # Remove or comment this line if you want to keep numbers
    text = remove_extra_spaces(text)
    
    return text

if __name__ == "__main__":
    print("مرحباً بك في أداة تنظيف وتطبيع النصوص العربية!")
    print("الآن سنقوم باختبار الأداة على بعض الأمثلة الشاملة.")
    
    test_cases = [
        "  كَيْفَ حالُكَ اليَوْمَ يا أَحْمَدُ؟ 123  ",
        "  هذه قِصَّةٌ رائعةٌ عن الألفةِ والأُسَرِ في عام 2024 !!!  ",
        "  أهلاً بِكَ في هذا الْمَشْروعِ التجريبي، ونتمنى لكَ التوفيقَ دائماً.  ",
        "أبراجُ الْمَمْلَكَةِ العَرَبِيَّةِ السُّعُودِيَّةِ.    " ,
        "السيارةُ تَقِفُ أماَمَ الْمنزلِ و الألِفُ والهمزةُ. أٌلْهِمَ الْعالِمُ. ٥٠٠ دولار."
    ]

    for i, original_text in enumerate(test_cases):
        cleaned_text = clean_and_normalize_arabic_text(original_text)
        print(f"\n--- حالة الاختبار {i+1} ---")
        print(f"النص الأصلي:\n'{original_text}'")
        print(f"النص بعد التنظيف والتطبيع:\n'{cleaned_text}'")
        print("-" * 50)
    
    print("\nالآن يمكنك تجريب الأداة بنفسك!")
    while True:
        user_input = input("أدخل نصاً للتنظيف (أو 'خروج' للمغادرة): ")
        if user_input.lower() == "خروج":
            print("شكراً لاستخدامك الأداة. إلى اللقاء!")
            break
        
        cleaned_text = clean_and_normalize_arabic_text(user_input)
        print("\nالنص بعد التنظيف والتطبيع:\n", cleaned_text)
        print("-" * 50)