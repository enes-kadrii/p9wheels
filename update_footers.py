import os

de_files = ['about.html', 'products.html', 'gallery.html', 'services.html', 'contact.html']
en_files = ['en/about.html', 'en/products.html', 'en/gallery.html', 'en/services.html', 'en/contact.html']

de_old = """    <footer>
        <div class="container footer-grid">
            <div class="footer-col">
                <div style="margin-bottom: 1.5rem;">
                    <img src="assets/images22/logo3.png" alt="P9 Wheels Logo" style="height: 120px; width: auto; object-fit: contain;">
                </div>
                <p>Schweizer Präzision. Unverkennbares Design. Kompromisslose Performance.</p>
            </div>
            
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="about.html">Über Uns</a></li>
                    <li><a href="products.html">Produkte</a></li>
                    <li><a href="gallery.html">Galerie</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="contact.html">Kontakt</a></li>
                </ul>
            </div>
            
            <div class="footer-col">
                <h4>Kontakt</h4>
                <p>info@p9wheels.ch</p>
                <p>+41 52 301 23 45</p>
                <div class="social-links" style="margin-top: 1rem;">
                    <a href="https://www.instagram.com/p9_wheels?igsh=MWZqcnluYmw4cW51NQ==" target="_blank" rel="noopener noreferrer"><i class="ph ph-instagram-logo"></i></a>
                </div>
            </div>
        </div>
        
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 P9 Wheels. Alle Rechte vorbehalten.</p>
            </div>
        </div>
    </footer>"""

de_new = """    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div style="margin-bottom: 1.5rem;">
                        <img src="assets/images22/logo3.png" alt="P9 Wheels Logo" style="height: 120px; width: auto; object-fit: contain;">
                    </div>
                    <p class="footer-desc">Premium Wheels. Swiss Precision. Die erste Wahl für Luxus- und Performance-Fahrzeuge.</p>
                    <div class="social-links">
                        <a href="https://www.instagram.com/p9_wheels?igsh=MWZqcnluYmw4cW51NQ==" target="_blank" rel="noopener noreferrer"><i class="ph ph-instagram-logo"></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="about.html">Über Uns</a></li>
                        <li><a href="products.html">Produkte</a></li>
                        <li><a href="gallery.html">Galerie</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="contact.html">Kontakt</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>Kontakt</h4>
                    <ul>
                        <li><i class="ph ph-map-pin"></i> Felgenwerk Andelfingen<br>Schaubenstrasse 1b<br>8450 Andelfingen, Schweiz</li>
                        <li><i class="ph ph-phone"></i> +41 76 321 50 05</li>
                        <li><i class="ph ph-envelope"></i> info@p9wheels.ch</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 P9 Wheels. Alle Rechte vorbehalten.</p>
                <div class="footer-legal">
                    <a href="#">Impressum</a>
                    <a href="#">Datenschutz</a>
                    <a href="#">AGB</a>
                </div>
            </div>
        </div>
    </footer>"""

en_old = """    <footer>
        <div class="container footer-grid">
            <div class="footer-col">
                <div style="margin-bottom: 1.5rem;">
                    <img src="../assets/images22/logo3.png" alt="P9 Wheels Logo" style="height: 120px; width: auto; object-fit: contain;">
                </div>
                <p>Swiss Precision. Unmistakable Design. Uncompromising Performance.</p>
            </div>
            
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="products.html">Products</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
            
            <div class="footer-col">
                <h4>Contact</h4>
                <p>info@p9wheels.ch</p>
                <p>+41 52 301 23 45</p>
                <div class="social-links" style="margin-top: 1rem;">
                    <a href="https://www.instagram.com/p9_wheels?igsh=MWZqcnluYmw4cW51NQ==" target="_blank" rel="noopener noreferrer"><i class="ph ph-instagram-logo"></i></a>
                </div>
            </div>
        </div>
        
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 P9 Wheels. All rights reserved.</p>
            </div>
        </div>
    </footer>"""

en_new = """    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div style="margin-bottom: 1.5rem;">
                        <img src="../assets/images22/logo3.png" alt="P9 Wheels Logo" style="height: 120px; width: auto; object-fit: contain;">
                    </div>
                    <p class="footer-desc">Premium Wheels. Swiss Precision. The first choice for luxury and performance vehicles.</p>
                    <div class="social-links">
                        <a href="https://www.instagram.com/p9_wheels?igsh=MWZqcnluYmw4cW51NQ==" target="_blank" rel="noopener noreferrer"><i class="ph ph-instagram-logo"></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="products.html">Products</a></li>
                        <li><a href="gallery.html">Gallery</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><i class="ph ph-map-pin"></i> Felgenwerk Andelfingen<br>Schaubenstrasse 1b<br>8450 Andelfingen, Switzerland</li>
                        <li><i class="ph ph-phone"></i> +41 76 321 50 05</li>
                        <li><i class="ph ph-envelope"></i> info@p9wheels.ch</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 P9 Wheels. All rights reserved.</p>
                <div class="footer-legal">
                    <a href="#">Imprint</a>
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms & Conditions</a>
                </div>
            </div>
        </div>
    </footer>"""

def replace_footer(file_path, old_content, new_content):
    if not os.path.exists(file_path):
        return f"Not found: {file_path}"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_content in content:
        content = content.replace(old_content, new_content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Updated: {file_path}"
    else:
        return f"Old footer not found in: {file_path}"

for f in de_files:
    print(replace_footer(f, de_old, de_new))
for f in en_files:
    print(replace_footer(f, en_old, en_new))
