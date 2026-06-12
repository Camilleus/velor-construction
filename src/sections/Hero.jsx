import React from 'react';
import { motion } from 'framer-motion';
import logoAlone from '../assets/veles-construction-logo-alone.png';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20">
      {/* Background Animated Signet */}
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 0.05, scale: 1 }}
        transition={{ duration: 2, ease: "easeOut" }}
        className="absolute inset-0 flex items-center justify-center pointer-events-none z-0"
      >
        <img src={logoAlone} alt="" className="w-[80vw] max-w-[1000px] object-contain rotate-[15deg] opacity-50" />
      </motion.div>

      <div className="container mx-auto px-6 relative z-10 text-center">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <span className="text-accent font-bold tracking-[0.3em] uppercase text-sm mb-6 block">
            Mazowsze, Polska
          </span>
          <h1 className="text-6xl md:text-[120px] font-display font-black leading-[0.8] uppercase mb-12 tracking-tighter">
            Solidność <br />
            <span className="text-white/20">
              Wpisana w beton
            </span>
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto text-lg md:text-xl mb-12 font-light leading-relaxed">
            Realizujemy luksusowe inwestycje, które definiują nowoczesne budownictwo.
            Precyzja rzemiosła połączona z industrialnym minimalizmem.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-6">
            <a
              href="#oferta"
              className="bg-accent text-white px-10 py-5 font-bold uppercase tracking-widest text-sm hover:bg-red-700 transition-all transform hover:-translate-y-1 shadow-[0_10px_30px_rgba(227,30,36,0.3)]"
            >
              Nasza Oferta
            </a>
            <a
              href="#kontakt"
              className="border border-white/20 px-10 py-5 font-bold uppercase tracking-widest text-sm hover:bg-white hover:text-black transition-all transform hover:-translate-y-1"
            >
              Kontakt
            </a>
          </div>
        </motion.div>
      </div>

      {/* Decorative lines */}
      <div className="absolute left-10 top-0 bottom-0 w-[1px] bg-white/5 hidden lg:block" />
      <div className="absolute right-10 top-0 bottom-0 w-[1px] bg-white/5 hidden lg:block" />
    </section>
  );
};

export default Hero;
