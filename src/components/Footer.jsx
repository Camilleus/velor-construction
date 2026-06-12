import React from 'react';
import logoFull from '../assets/veles-construction-full.png';

const Footer = () => {
  return (
    <footer className="bg-black py-20 border-t border-white/5">
      <div className="container mx-auto px-6">
        <div className="grid md:grid-cols-4 gap-12 mb-20">

          <div className="md:col-span-2">
            <img src={logoFull} alt="Veles Construction" className="h-20 w-auto mb-8 grayscale brightness-200" />
            <p className="text-gray-500 max-w-sm text-sm leading-relaxed uppercase tracking-widest font-medium">
              Mazowiecki lider w budownictwie przemysłowym i luksusowym.
              Tworzymy przestrzenie, które wytrzymają próbę czasu.
            </p>
          </div>

          <div>
            <h4 className="text-white font-bold uppercase tracking-[0.2em] text-xs mb-8">Nawigacja</h4>
            <ul className="space-y-4">
              <li><a href="#" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Home</a></li>
              <li><a href="#oferta" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Nasza Oferta</a></li>
              <li><a href="#kariera" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Kariera</a></li>
              <li><a href="#kontakt" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Kontakt</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-white font-bold uppercase tracking-[0.2em] text-xs mb-8">Social Media</h4>
            <ul className="space-y-4">
              <li><a href="#" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">LinkedIn</a></li>
              <li><a href="#" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Instagram</a></li>
              <li><a href="#" className="text-gray-500 hover:text-white transition-colors uppercase text-xs tracking-widest">Facebook</a></li>
            </ul>
          </div>

        </div>

        <div className="flex flex-col md:flex-row justify-between items-center pt-8 border-t border-white/5 gap-6">
          <p className="text-[10px] text-gray-600 uppercase tracking-[0.2em]">
            © 2025 Veles Construction. Wszystkie prawa zastrzeżone.
          </p>
          <div className="flex gap-10">
            <a href="#" className="text-[10px] text-gray-600 uppercase tracking-[0.2em] hover:text-white">Polityka Prywatności</a>
            <a href="#" className="text-[10px] text-gray-600 uppercase tracking-[0.2em] hover:text-white">Regulamin</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
