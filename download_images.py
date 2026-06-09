from bing_image_downloader import downloader
import os
keywords = {
    'cam': ['glass bottle', 'glass jar', 'broken glass', 'wine bottle glass'],
    'kagit': ['paper box', 'cardboard box', 'newspaper', 'magazine paper', 'paper bag'],
    'metal': ['aluminum can', 'tin can', 'metal container', 'steel can'],
    'plastik': ['plastic bottle', 'plastic container', 'plastic cup', 'plastic bag', 'milk jug plastic']
}

output_base_dir = 'C:/GeriDonusum/dataset/'
for category, search_terms in keywords.items():
    category_dir = os.path.join(output_base_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

    print(f"\n--- Resimler İndiriliyor: {category.upper()} ---")
    for term in search_terms:
        print(f"  Anahtar Kelime: {term}")
        try:
            downloader.download(
                query=term,
                limit=200, 
                output_dir=category_dir,
                adult_filter_off=True,
                force_replace=False, 
                timeout=60 
            )
        except Exception as e:
            print(f"    Hata oluştu '{term}' için: {e}")
print("\nTüm resim indirme işlemleri tamamlandı!")