import { useState, useEffect } from 'react';
import { motion, AnimatePresence, useScroll, useTransform } from 'framer-motion';
import { Menu, X, ChevronRight, HardHat, Ruler, Briefcase, MapPin, Phone, Mail, Send, ArrowRight } from 'lucide-react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// --- Components ---

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('hero');

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);

      const sections = ['hero', 'oferta', 'kariera', 'kontakt'];
      const current = sections.find(section => {
        const element = document.getElementById(section);
        if (element) {
          const rect = element.getBoundingClientRect();
          return rect.top <= 100 && rect.bottom >= 100;
        }
        return false;
      });
      if (current) setActiveSection(current);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Start', href: '#hero', id: 'hero' },
    { name: 'Oferta', href: '#oferta', id: 'oferta' },
    { name: 'Kariera', href: '#kariera', id: 'kariera' },
    { name: 'Kontakt', href: '#kontakt', id: 'kontakt' },
  ];

  return (
    <nav className={cn(
      "fixed top-0 left-0 w-full z-50 transition-all duration-500 px-6 py-4 md:px-12 md:py-6",
      isScrolled ? "bg-[#0a0a0a]/90 backdrop-blur-md border-b border-white/10" : "bg-transparent"
    )}>
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <motion.a
          href="#hero"
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="text-2xl md:text-3xl font-black tracking-tighter font-montserrat flex items-center gap-1"
        >
          VELES<span className="text-primary text-4xl">.</span>
        </motion.a>

        {/* Desktop Menu */}
        <div className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className={cn(
                "text-sm uppercase tracking-widest font-bold transition-colors relative group",
                activeSection === link.id ? "text-primary" : "text-white/60 hover:text-white"
              )}
            >
              {link.name}
              <span className={cn(
                "absolute -bottom-1 left-0 h-[2px] bg-primary transition-all duration-300",
                activeSection === link.id ? "w-full" : "w-0 group-hover:w-full"
              )} />
            </a>
          ))}
        </div>

        {/* Mobile Toggle */}
        <button
          className="md:hidden text-white"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          {isMobileMenuOpen ? <X size={32} /> : <Menu size={32} />}
        </button>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="absolute top-full left-0 w-full bg-[#0a0a0a] border-b border-white/10 p-8 flex flex-col gap-6 md:hidden"
          >
            {navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                onClick={() => setIsMobileMenuOpen(false)}
                className="text-2xl font-black font-montserrat uppercase tracking-tighter text-white hover:text-primary transition-colors"
              >
                {link.name}
              </a>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
};

const Hero = () => {
  const { scrollY } = useScroll();
  const y1 = useTransform(scrollY, [0, 500], [0, 200]);
  const opacity = useTransform(scrollY, [0, 300], [1, 0]);

  return (
    <section id="hero" className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20">
      {/* Animated V Sygnet in Background */}
      <motion.div
        style={{ y: y1, opacity }}
        className="absolute inset-0 flex items-center justify-center pointer-events-none select-none overflow-hidden"
      >
        <div className="relative w-full max-w-4xl opacity-[0.03]">
          <svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-auto">
            <path d="M10 10L50 90L90 10" stroke="white" strokeWidth="2" strokeLinejoin="miter"/>
          </svg>
        </div>
      </motion.div>

      <div className="relative z-10 max-w-7xl mx-auto px-6 text-center">
        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="text-5xl md:text-8xl lg:text-9xl font-black font-montserrat leading-tight tracking-tighter mb-8"
        >
          BUDUJEMY <br />
          <span className="text-primary italic">PRZYSZŁOŚĆ.</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="text-lg md:text-xl text-white/40 max-w-2xl mx-auto mb-12 uppercase tracking-[0.2em] font-medium"
        >
          Precyzja industrialna. Minimalizm luksusowy. <br /> Generalne wykonawstwo najwyższej klasy.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <a
            href="#oferta"
            className="group relative inline-flex items-center gap-4 bg-primary px-10 py-5 font-black text-lg uppercase tracking-tighter hover:bg-white hover:text-black transition-all duration-500"
          >
            Nasze Usługi
            <ArrowRight className="group-hover:translate-x-2 transition-transform duration-300" />
          </a>
        </motion.div>
      </div>

      {/* Scroll Indicator */}
      <motion.div
        animate={{ y: [0, 10, 0] }}
        transition={{ duration: 2, repeat: Infinity }}
        className="absolute bottom-10 left-1/2 -translate-x-1/2 text-white/20"
      >
        <div className="w-[1px] h-16 bg-white/20 mx-auto mb-4 relative overflow-hidden">
           <motion.div
            animate={{ y: [-64, 64] }}
            transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
            className="absolute top-0 left-0 w-full h-full bg-primary"
           />
        </div>
        <span className="text-[10px] uppercase tracking-[0.4em] font-bold">Scroll</span>
      </motion.div>
    </section>
  );
};

const Oferta = () => {
  const [expanded, setExpanded] = useState<number | null>(null);

  const services = [
    {
      title: "Generalne Wykonawstwo",
      icon: <HardHat className="text-primary" size={40} />,
      desc: "Kompleksowa realizacja inwestycji od fundamentów po dach. Zarządzamy każdym etapem budowy, gwarantując terminowość i najwyższe standardy jakościowe.",
      details: ["Nadzór inżynierski", "Logistyka materiałowa", "Zarządzanie podwykonawcami"]
    },
    {
      title: "Projektowanie Industrialne",
      icon: <Ruler className="text-primary" size={40} />,
      desc: "Tworzymy projekty, które łączą surowy charakter industrialny z nowoczesną funkcjonalnością. Architektura, która przetrwa próbę czasu.",
      details: ["Projekty architektoniczne", "Design wnętrz", "Optymalizacja kosztów"]
    },
    {
      title: "Zarządzanie Inwestycją",
      icon: <Briefcase className="text-primary" size={40} />,
      desc: "Profesjonalne zastępstwo inwestorskie. Reprezentujemy Twoje interesy na budowie, dbając o budżet i zgodność z projektem.",
      details: ["Analiza finansowa", "Kontrola jakości", "Doradztwo techniczne"]
    }
  ];

  return (
    <section id="oferta" className="py-24 md:py-40 bg-[#0a0a0a]">
      <div className="max-w-7xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <span className="text-primary font-bold tracking-[0.3em] uppercase text-sm">/ Usługi</span>
          <h2 className="text-4xl md:text-6xl font-black font-montserrat mt-4 tracking-tighter uppercase">Definiujemy <br /><span className="text-white/20">Nowy Standard.</span></h2>
        </motion.div>

        <div className="grid grid-cols-1 gap-6">
          {services.map((service, index) => (
            <motion.div
              key={index}
              layout
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              onClick={() => setExpanded(expanded === index ? null : index)}
              className={cn(
                "group border border-white/5 bg-[#111] p-8 md:p-12 cursor-pointer transition-all duration-500 hover:border-primary/50 relative overflow-hidden",
                expanded === index ? "border-primary" : ""
              )}
            >
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-8">
                <div className="flex items-center gap-8">
                  <span className="text-6xl md:text-8xl font-black font-montserrat text-white/5 group-hover:text-primary/10 transition-colors">0{index + 1}</span>
                  <div>
                    <h3 className="text-2xl md:text-3xl font-black font-montserrat uppercase tracking-tight mb-2">{service.title}</h3>
                    <p className="text-white/40 max-w-xl">{service.desc}</p>
                  </div>
                </div>
                <div className="flex items-center justify-between md:justify-end gap-4">
                   <div className="bg-white/5 p-4 rounded-full group-hover:bg-primary transition-colors">
                      {service.icon}
                   </div>
                   <motion.div
                    animate={{ rotate: expanded === index ? 180 : 0 }}
                    className="text-white/20"
                   >
                     <ChevronRight size={32} />
                   </motion.div>
                </div>
              </div>

              <AnimatePresence>
                {expanded === index && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    className="overflow-hidden"
                  >
                    <div className="pt-12 mt-12 border-t border-white/5 grid grid-cols-1 md:grid-cols-3 gap-8">
                      {service.details.map((detail, i) => (
                        <div key={i} className="flex items-center gap-4">
                          <div className="w-2 h-2 bg-primary" />
                          <span className="text-sm font-bold uppercase tracking-widest text-white/80">{detail}</span>
                        </div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

const Kariera = () => {
  const jobs = [
    { title: "Kierownik Budowy", location: "Wrocław / Hybrydowo", type: "B2B / UoP" },
    { title: "Architekt Wnętrz", location: "Warszawa", type: "B2B" },
    { title: "Inżynier Kontraktu", location: "Poznań", type: "UoP" },
  ];

  const [applyOpen, setApplyOpen] = useState<string | null>(null);

  return (
    <section id="kariera" className="py-24 md:py-40 bg-[#0a0a0a] border-y border-white/5">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-end gap-8 mb-20">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="text-primary font-bold tracking-[0.3em] uppercase text-sm">/ Kariera</span>
            <h2 className="text-4xl md:text-6xl font-black font-montserrat mt-4 tracking-tighter uppercase">Buduj z Nami.</h2>
          </motion.div>
          <p className="text-white/40 max-w-sm md:text-right">Poszukujemy ekspertów, którzy nie boją się wyzwań i cenią industrialną precyzję.</p>
        </div>

        <div className="space-y-4">
          {jobs.map((job, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="group bg-[#111] p-6 md:p-10 flex flex-col md:flex-row md:items-center justify-between border border-transparent hover:border-primary transition-all duration-300"
            >
              <div className="mb-6 md:mb-0">
                <h3 className="text-xl md:text-2xl font-black uppercase tracking-tight mb-2">{job.title}</h3>
                <div className="flex gap-6 text-sm text-white/30 uppercase tracking-widest font-bold">
                  <span className="flex items-center gap-2"><MapPin size={14} /> {job.location}</span>
                  <span className="flex items-center gap-2"><Briefcase size={14} /> {job.type}</span>
                </div>
              </div>
              <button
                onClick={() => setApplyOpen(job.title)}
                className="inline-flex items-center justify-center gap-4 bg-white text-black px-8 py-4 font-black uppercase tracking-tighter group-hover:bg-primary group-hover:text-white transition-colors"
              >
                Aplikuj
                <ChevronRight size={20} />
              </button>
            </motion.div>
          ))}
        </div>

        <AnimatePresence>
          {applyOpen && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/90 backdrop-blur-xl"
            >
              <motion.div
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.9, opacity: 0 }}
                className="bg-[#111] border border-white/10 p-8 md:p-12 max-w-lg w-full relative"
              >
                <button onClick={() => setApplyOpen(null)} className="absolute top-6 right-6 text-white/40 hover:text-white"><X /></button>
                <h3 className="text-3xl font-black uppercase tracking-tight mb-2">Quick Apply</h3>
                <p className="text-white/40 mb-8 uppercase tracking-widest text-xs font-bold">Aplikujesz na: <span className="text-primary">{applyOpen}</span></p>

                <form className="space-y-4">
                  <input type="text" placeholder="Imię i Nazwisko" className="w-full bg-white/5 border border-white/10 px-6 py-4 focus:border-primary outline-none text-white font-bold transition-colors" />
                  <input type="email" placeholder="Email" className="w-full bg-white/5 border border-white/10 px-6 py-4 focus:border-primary outline-none text-white font-bold transition-colors" />
                  <div className="border-2 border-dashed border-white/10 p-8 text-center cursor-pointer hover:border-primary transition-colors">
                    <p className="text-white/20 uppercase tracking-widest text-xs font-black">Załącz CV (PDF)</p>
                  </div>
                  <button className="w-full bg-primary py-5 font-black uppercase tracking-widest hover:bg-white hover:text-black transition-all duration-300">Wyślij Aplikację</button>
                </form>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
};

const Kontakt = () => {
  return (
    <section id="kontakt" className="py-24 md:py-40 bg-[#0a0a0a]">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-20">
          <motion.div
             initial={{ opacity: 0, x: -50 }}
             whileInView={{ opacity: 1, x: 0 }}
             viewport={{ once: true }}
          >
            <span className="text-primary font-bold tracking-[0.3em] uppercase text-sm">/ Kontakt</span>
            <h2 className="text-5xl md:text-7xl font-black font-montserrat mt-4 tracking-tighter uppercase mb-12">Porozmawiajmy <br /> o Twym <span className="text-white/20 italic">Projekcie.</span></h2>

            <div className="space-y-12">
              <div className="flex items-start gap-6">
                <div className="p-4 bg-white/5 text-primary"><MapPin size={24} /></div>
                <div>
                  <h4 className="text-xs uppercase tracking-[0.3em] font-black text-white/30 mb-2">Adres</h4>
                  <p className="text-xl font-bold font-montserrat">ul. Industrialna 24, <br /> 50-001 Wrocław</p>
                </div>
              </div>
              <div className="flex items-start gap-6">
                <div className="p-4 bg-white/5 text-primary"><Phone size={24} /></div>
                <div>
                  <h4 className="text-xs uppercase tracking-[0.3em] font-black text-white/30 mb-2">Telefon</h4>
                  <p className="text-xl font-bold font-montserrat">+48 71 000 00 00</p>
                </div>
              </div>
              <div className="flex items-start gap-6">
                <div className="p-4 bg-white/5 text-primary"><Mail size={24} /></div>
                <div>
                  <h4 className="text-xs uppercase tracking-[0.3em] font-black text-white/30 mb-2">Email</h4>
                  <p className="text-xl font-bold font-montserrat">biuro@velesconstruction.pl</p>
                </div>
              </div>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="bg-[#111] p-8 md:p-16 border border-white/5"
          >
            <form className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <label className="text-[10px] uppercase tracking-widest font-black text-white/40">Imię i Nazwisko</label>
                  <input type="text" className="w-full bg-transparent border-b border-white/10 py-4 focus:border-primary outline-none transition-colors" />
                </div>
                <div className="space-y-2">
                  <label className="text-[10px] uppercase tracking-widest font-black text-white/40">Email</label>
                  <input type="email" className="w-full bg-transparent border-b border-white/10 py-4 focus:border-primary outline-none transition-colors" />
                </div>
              </div>
              <div className="space-y-2">
                  <label className="text-[10px] uppercase tracking-widest font-black text-white/40">Usługa</label>
                  <select className="w-full bg-transparent border-b border-white/10 py-4 focus:border-primary outline-none transition-colors appearance-none text-white/60">
                    <option className="bg-[#111]">Generalne Wykonawstwo</option>
                    <option className="bg-[#111]">Projektowanie</option>
                    <option className="bg-[#111]">Zarządzanie</option>
                  </select>
              </div>
              <div className="space-y-2">
                <label className="text-[10px] uppercase tracking-widest font-black text-white/40">Wiadomość</label>
                <textarea rows={4} className="w-full bg-transparent border-b border-white/10 py-4 focus:border-primary outline-none transition-colors resize-none" />
              </div>
              <button className="group w-full bg-white text-black py-6 font-black uppercase tracking-widest flex items-center justify-center gap-4 hover:bg-primary hover:text-white transition-all duration-500">
                Wyślij Zapytanie
                <Send size={20} className="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
              </button>
            </form>
          </motion.div>
        </div>

        {/* Map Placeholder */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-20 h-96 bg-[#111] border border-white/5 relative overflow-hidden grayscale contrast-125"
        >
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
               <MapPin size={48} className="text-primary mx-auto mb-4" />
               <span className="text-white/20 uppercase tracking-[0.5em] font-black">Interaktywna Mapa</span>
            </div>
          </div>
          {/* Simple grid lines to look "architectural" */}
          <div className="absolute inset-0 opacity-10 pointer-events-none"
               style={{ backgroundImage: 'radial-gradient(circle, white 1px, transparent 1px)', backgroundSize: '40px 40px' }} />
        </motion.div>
      </div>
    </section>
  );
};

const Footer = () => {
  return (
    <footer className="py-20 bg-[#050505] border-t border-white/5">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-12">
          <div>
            <a href="#hero" className="text-4xl font-black tracking-tighter font-montserrat">
              VELES<span className="text-primary">.</span>
            </a>
            <p className="text-white/20 mt-4 max-w-xs font-medium uppercase tracking-widest text-[10px]">
              Veles Construction Sp. z o.o. <br />
              Wszystkie prawa zastrzeżone © 2024
            </p>
          </div>

          <div className="flex gap-12">
            <div className="flex flex-col gap-4">
              <span className="text-[10px] uppercase tracking-widest font-black text-primary">Nawigacja</span>
              <a href="#hero" className="text-white/40 hover:text-white transition-colors text-sm font-bold uppercase tracking-tight">Start</a>
              <a href="#oferta" className="text-white/40 hover:text-white transition-colors text-sm font-bold uppercase tracking-tight">Oferta</a>
            </div>
            <div className="flex flex-col gap-4">
              <span className="text-[10px] uppercase tracking-widest font-black text-primary">Social</span>
              <a href="#" className="text-white/40 hover:text-white transition-colors text-sm font-bold uppercase tracking-tight">LinkedIn</a>
              <a href="#" className="text-white/40 hover:text-white transition-colors text-sm font-bold uppercase tracking-tight">Instagram</a>
            </div>
          </div>

          <div className="md:text-right">
             <p className="text-white/60 font-black uppercase tracking-tighter text-xl">Precyzja w każdym <br /> centymetrze.</p>
          </div>
        </div>
      </div>
    </footer>
  );
};

const App = () => {
  return (
    <div className="bg-[#0a0a0a] text-white font-sans selection:bg-primary selection:text-white">
      <Navbar />
      <main>
        <Hero />
        <Oferta />
        <Kariera />
        <Kontakt />
      </main>
      <Footer />
    </div>
  );
};

export default App;
