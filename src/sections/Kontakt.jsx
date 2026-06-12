import React from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, ArrowUpRight } from 'lucide-react';

const Kontakt = () => {
  return (
    <section id="kontakt" className="py-24 bg-background border-t border-white/5">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="container mx-auto px-6"
      >
        <div className="grid lg:grid-cols-2 gap-20">

          {/* Info Side */}
          <div>
            <span className="text-accent font-bold tracking-[0.2em] uppercase text-xs">/ Kontakt</span>
            <h2 className="text-4xl md:text-6xl font-black uppercase mt-4 mb-12">
              Zaplanujmy <br />
              <span className="text-white/20">Twoją Inwestycję</span>
            </h2>

            <div className="space-y-10">
              <div className="flex gap-6 group">
                <div className="w-12 h-12 bg-white/5 flex items-center justify-center text-accent group-hover:bg-accent group-hover:text-white transition-colors">
                  <MapPin size={24} />
                </div>
                <div>
                  <p className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold mb-1">Adres Biura</p>
                  <p className="text-xl font-bold uppercase">ul. Emilii Plater 53, Warszawa</p>
                  <p className="text-gray-400">00-113 Mazowieckie, Polska</p>
                </div>
              </div>

              <div className="flex gap-6 group">
                <div className="w-12 h-12 bg-white/5 flex items-center justify-center text-accent group-hover:bg-accent group-hover:text-white transition-colors">
                  <Phone size={24} />
                </div>
                <div>
                  <p className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold mb-1">Telefon</p>
                  <p className="text-xl font-bold uppercase">+48 500 600 700</p>
                  <p className="text-gray-400">Pon - Pt: 08:00 - 18:00</p>
                </div>
              </div>

              <div className="flex gap-6 group">
                <div className="w-12 h-12 bg-white/5 flex items-center justify-center text-accent group-hover:bg-accent group-hover:text-white transition-colors">
                  <Mail size={24} />
                </div>
                <div>
                  <p className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold mb-1">Email</p>
                  <p className="text-xl font-bold uppercase">biuro@veles.pl</p>
                  <p className="text-gray-400">Zapytania ofertowe</p>
                </div>
              </div>
            </div>

            {/* Map Placeholder */}
            <div className="mt-16 h-64 bg-white/5 border border-white/10 relative overflow-hidden group">
              <div className="absolute inset-0 grayscale opacity-30 group-hover:opacity-50 transition-opacity flex items-center justify-center">
                 <MapPin size={48} className="text-accent" />
                 <span className="ml-4 font-black uppercase tracking-widest text-white/10 text-4xl">MAPA INTERAKTYWNA</span>
              </div>
              <div className="absolute bottom-6 left-6 bg-background border border-white/10 p-4">
                <p className="text-[10px] font-bold uppercase tracking-widest text-accent mb-1">Lokalizacja</p>
                <p className="text-xs text-gray-400">Kliknij aby otworzyć w Google Maps</p>
              </div>
              <a href="#" className="absolute inset-0 z-10" />
            </div>
          </div>

          {/* Form Side */}
          <div className="bg-[#111] p-8 md:p-12 border border-white/10 relative">
            <div className="absolute -top-[1px] -right-[1px] w-12 h-12 border-t-2 border-r-2 border-accent" />

            <form className="space-y-8">
              <div className="grid md:grid-cols-2 gap-8">
                <div>
                  <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">Imię</label>
                  <input type="text" className="w-full bg-transparent border-b border-white/10 py-3 outline-none focus:border-accent transition-colors" />
                </div>
                <div>
                  <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">Nazwisko</label>
                  <input type="text" className="w-full bg-transparent border-b border-white/10 py-3 outline-none focus:border-accent transition-colors" />
                </div>
              </div>

              <div>
                <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">Temat Wiadomości</label>
                <select className="w-full bg-transparent border-b border-white/10 py-3 outline-none focus:border-accent transition-colors appearance-none">
                  <option className="bg-[#111]">Wycena Projektu</option>
                  <option className="bg-[#111]">Współpraca</option>
                  <option className="bg-[#111]">Inne</option>
                </select>
              </div>

              <div>
                <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">Twoja Wiadomość</label>
                <textarea rows="4" className="w-full bg-transparent border-b border-white/10 py-3 outline-none focus:border-accent transition-colors resize-none"></textarea>
              </div>

              <div className="flex items-start gap-4">
                <input type="checkbox" id="consent" className="mt-1 accent-accent" />
                <label htmlFor="consent" className="text-[10px] text-gray-500 leading-relaxed uppercase tracking-wider">
                  Wyrażam zgodę na przetwarzanie danych osobowych zgodnie z polityką prywatności firmy Veles Construction.
                </label>
              </div>

              <button className="group w-full bg-white text-black py-6 font-black uppercase tracking-[0.2em] text-sm flex items-center justify-center gap-4 hover:bg-accent hover:text-white transition-all">
                Wyślij Zapytanie
                <ArrowUpRight size={20} className="group-hover:rotate-45 transition-transform" />
              </button>
            </form>
          </div>

        </div>
      </motion.div>
    </section>
  );
};

export default Kontakt;
