import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronDown, HardHat, Ruler, Building2 } from 'lucide-react';

const services = [
  {
    id: 'general',
    title: 'Generalne Wykonawstwo',
    icon: <Building2 className="w-8 h-8" />,
    short: 'Kompleksowa realizacja inwestycji od fundamentów po dach.',
    details: 'Zapewniamy kompleksowe zarządzanie procesem budowlanym, logistykę materiałową oraz rygorystyczny nadzór techniczny. Nasze doświadczenie na terenie Mazowsza gwarantuje terminowość i najwyższą jakość wykonania stanów surowych oraz deweloperskich.',
  },
  {
    id: 'design',
    title: 'Projektowanie i Konsultacje',
    icon: <Ruler className="w-8 h-8" />,
    short: 'Architektoniczne wizje przekute w techniczne plany.',
    details: 'Współpracujemy z czołowymi architektami, aby dostarczać projekty, które są nie tylko piękne, ale i funkcjonalne. Optymalizujemy koszty już na etapie koncepcji, dbając o każdy milimetr przestrzeni.',
  },
  {
    id: 'management',
    title: 'Zarządzanie Projektami',
    icon: <HardHat className="w-8 h-8" />,
    short: 'Pełna kontrola nad harmonogramem i budżetem.',
    details: 'Reprezentujemy inwestora na każdym etapie. Od pozwoleń prawnych, przez wybór podwykonawców, aż po finalne odbiory. Transparentność i raportowanie to nasze fundamenty.',
  },
];

const ServiceCard = ({ service, isOpen, onClick }) => {
  return (
    <motion.div
      layout
      className={`bg-[#111] border ${isOpen ? 'border-accent' : 'border-white/5'} p-8 cursor-pointer group transition-colors`}
      onClick={onClick}
    >
      <div className="flex justify-between items-start mb-6">
        <div className={`p-4 ${isOpen ? 'bg-accent text-white' : 'bg-white/5 text-accent'} group-hover:bg-accent group-hover:text-white transition-colors`}>
          {service.icon}
        </div>
        <motion.div
          animate={{ rotate: isOpen ? 180 : 0 }}
          className="text-white/30 group-hover:text-white transition-colors"
        >
          <ChevronDown />
        </motion.div>
      </div>

      <motion.h3 layout="position" className="text-2xl font-bold uppercase mb-4 tracking-tight">
        {service.title}
      </motion.h3>

      <motion.p layout="position" className="text-gray-400 mb-4 leading-relaxed">
        {service.short}
      </motion.p>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="overflow-hidden"
          >
            <div className="pt-6 border-t border-white/10 text-gray-300 text-sm leading-relaxed">
              {service.details}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

const Oferta = () => {
  const [openId, setOpenId] = useState(null);

  return (
    <section id="oferta" className="py-24 bg-background overflow-hidden">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="container mx-auto px-6"
      >
        <div className="mb-16">
          <span className="text-accent font-bold tracking-[0.2em] uppercase text-xs">/ Usługi</span>
          <h2 className="text-4xl md:text-6xl font-black uppercase mt-4 mb-8">
            Zakres <span className="text-white/20">Działań</span>
          </h2>
          <div className="w-20 h-1 bg-accent" />
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {services.map((service) => (
            <ServiceCard
              key={service.id}
              service={service}
              isOpen={openId === service.id}
              onClick={() => setOpenId(openId === service.id ? null : service.id)}
            />
          ))}
        </div>
      </motion.div>
    </section>
  );
};

export default Oferta;
