import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Briefcase, Send, X } from 'lucide-react';

const jobs = [
  { id: 1, title: 'Kierownik Budowy', location: 'Warszawa / Mazowieckie', type: 'Pełny etat' },
  { id: 2, title: 'Inżynier Projektu', location: 'Warszawa', type: 'Kontrakt / B2B' },
  { id: 3, title: 'Brygadzista', location: 'Mazowsze (Różne lokalizacje)', type: 'Pełny etat' },
];

const Kariera = () => {
  const [selectedJob, setSelectedJob] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setTimeout(() => {
      setIsSubmitting(false);
      setSelectedJob(null);
      alert('Aplikacja została wysłana! Skontaktujemy się z Tobą wkrótce.');
    }, 1500);
  };

  return (
    <section id="kariera" className="py-24 bg-background relative">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="container mx-auto px-6"
      >
        <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
          <div>
            <span className="text-accent font-bold tracking-[0.2em] uppercase text-xs">/ Zespół</span>
            <h2 className="text-4xl md:text-6xl font-black uppercase mt-4">
              Buduj z <span className="text-white/20">Nami</span>
            </h2>
          </div>
          <p className="text-gray-400 max-w-md text-sm md:text-base">
            Szukamy profesjonalistów, którzy nie boją się wyzwań i cenią industrialną precyzję. Dołącz do lidera rynku premium.
          </p>
        </div>

        <div className="space-y-4">
          {jobs.map((job) => (
            <motion.div
              key={job.id}
              whileHover={{ x: 10 }}
              className="bg-[#111] border border-white/5 p-6 md:p-8 flex flex-col md:flex-row justify-between items-center group cursor-pointer hover:border-accent transition-colors"
              onClick={() => setSelectedJob(job)}
            >
              <div className="flex items-center gap-6 mb-4 md:mb-0">
                <div className="p-3 bg-white/5 text-white/40 group-hover:bg-accent group-hover:text-white transition-colors">
                  <Briefcase size={24} />
                </div>
                <div>
                  <h3 className="text-xl font-bold uppercase tracking-tight">{job.title}</h3>
                  <p className="text-gray-500 text-sm">{job.location}</p>
                </div>
              </div>
              <div className="flex items-center gap-8">
                <span className="text-xs font-bold uppercase tracking-widest text-gray-500 border border-white/10 px-3 py-1">
                  {job.type}
                </span>
                <span className="text-accent font-bold uppercase text-xs tracking-[0.2em] group-hover:translate-x-2 transition-transform">
                  Aplikuj →
                </span>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Quick Apply Modal */}
      <AnimatePresence>
        {selectedJob && (
          <div className="fixed inset-0 z-[100] flex items-center justify-center p-6">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="absolute inset-0 bg-black/90 backdrop-blur-sm"
              onClick={() => setSelectedJob(null)}
            />
            <motion.div
              initial={{ scale: 0.9, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.9, opacity: 0, y: 20 }}
              className="relative bg-[#111] border border-white/10 p-8 md:p-12 max-w-lg w-full"
            >
              <button
                className="absolute top-6 right-6 text-white/30 hover:text-white"
                onClick={() => setSelectedJob(null)}
              >
                <X />
              </button>

              <h3 className="text-2xl font-black uppercase mb-2">Szybka Aplikacja</h3>
              <p className="text-accent text-sm font-bold uppercase tracking-widest mb-8">
                Rola: {selectedJob.title}
              </p>

              <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                  <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">
                    Imię i Nazwisko
                  </label>
                  <input
                    required
                    type="text"
                    className="w-full bg-white/5 border border-white/10 p-4 focus:border-accent outline-none transition-colors text-white"
                  />
                </div>
                <div>
                  <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">
                    Email Kontaktowy
                  </label>
                  <input
                    required
                    type="email"
                    className="w-full bg-white/5 border border-white/10 p-4 focus:border-accent outline-none transition-colors text-white"
                  />
                </div>
                <div>
                  <label className="block text-[10px] uppercase tracking-[0.2em] text-gray-500 mb-2 font-bold">
                    Link do Portfolio / LinkedIn
                  </label>
                  <input
                    type="text"
                    className="w-full bg-white/5 border border-white/10 p-4 focus:border-accent outline-none transition-colors text-white"
                  />
                </div>
                <button
                  disabled={isSubmitting}
                  type="submit"
                  className="w-full bg-accent text-white py-5 font-bold uppercase tracking-widest text-sm flex items-center justify-center gap-3 hover:bg-red-700 transition-colors disabled:opacity-50"
                >
                  {isSubmitting ? 'Wysyłanie...' : (
                    <>
                      Wyślij Aplikację <Send size={16} />
                    </>
                  )}
                </button>
              </form>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </section>
  );
};

export default Kariera;
